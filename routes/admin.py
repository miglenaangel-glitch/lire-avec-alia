import os
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session, current_app
from werkzeug.utils import secure_filename

admin_bp = Blueprint('admin', __name__)

ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'laykuchka2026')
ALLOWED_IMAGE = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
ALLOWED_VIDEO = {'mp4', 'mov', 'webm'}


def allowed_file(filename, types):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in types


def get_mysql():
    return current_app.extensions['mysql']


def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated


@admin_bp.route('/laykuchka/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form.get('password') == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin.dashboard'))
        error = 'Mot de passe incorrect.'
    return render_template('admin/login.html', error=error)


@admin_bp.route('/laykuchka/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin.login'))


@admin_bp.route('/laykuchka/')
@admin_required
def dashboard():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(*) as n FROM postcards WHERE is_active=TRUE")
    pc_count = cur.fetchone()['n']
    cur.execute("SELECT COUNT(*) as n FROM mailbox")
    mb_count = cur.fetchone()['n']
    cur.execute("SELECT COUNT(*) as n FROM daily_reports")
    rp_count = cur.fetchone()['n']
    cur.close()

    # List videos
    video_dir = os.path.join(current_app.static_folder, 'videos')
    videos = []
    if os.path.exists(video_dir):
        videos = [f for f in os.listdir(video_dir) if f.rsplit('.', 1)[-1].lower() in ALLOWED_VIDEO]

    return render_template('admin/dashboard.html',
        pc_count=pc_count, mb_count=mb_count, rp_count=rp_count, videos=videos)


# ── POSTCARDS ──
@admin_bp.route('/laykuchka/postcards')
@admin_required
def postcards():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM postcards ORDER BY created_at DESC")
    cards = cur.fetchall()
    cur.close()
    return render_template('admin/postcards.html', cards=cards)


@admin_bp.route('/laykuchka/postcards/upload', methods=['POST'])
@admin_required
def upload_postcard():
    if 'image' not in request.files:
        return jsonify({'error': 'No file'}), 400
    f = request.files['image']
    label = request.form.get('label', '').strip()
    if not f.filename or not allowed_file(f.filename, ALLOWED_IMAGE):
        return jsonify({'error': 'Format non supporté'}), 400

    filename = secure_filename(f.filename)
    save_path = os.path.join(current_app.static_folder, 'postcards', filename)
    f.save(save_path)

    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO postcards (image_path, label) VALUES (%s, %s)",
                (f'postcards/{filename}', label))
    mysql.connection.commit()
    new_id = cur.lastrowid
    cur.close()
    return jsonify({'success': True, 'id': new_id, 'filename': filename})


@admin_bp.route('/laykuchka/postcards/delete/<int:pc_id>', methods=['POST'])
@admin_required
def delete_postcard(pc_id):
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT image_path FROM postcards WHERE id = %s", (pc_id,))
    row = cur.fetchone()
    cur.execute("UPDATE postcards SET is_active = FALSE WHERE id = %s", (pc_id,))
    mysql.connection.commit()
    cur.close()
    # Optionally delete file
    if row:
        fp = os.path.join(current_app.static_folder, row['image_path'])
        if os.path.exists(fp):
            os.remove(fp)
    return jsonify({'success': True})


# ── VIDEOS ──
@admin_bp.route('/laykuchka/videos')
@admin_required
def videos():
    video_dir = os.path.join(current_app.static_folder, 'videos')
    os.makedirs(video_dir, exist_ok=True)
    files = [f for f in os.listdir(video_dir) if f.rsplit('.', 1)[-1].lower() in ALLOWED_VIDEO]
    return render_template('admin/videos.html', videos=files)


@admin_bp.route('/laykuchka/videos/upload', methods=['POST'])
@admin_required
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No file'}), 400
    f = request.files['video']
    if not f.filename or not allowed_file(f.filename, ALLOWED_VIDEO):
        return jsonify({'error': 'Format non supporté'}), 400
    filename = secure_filename(f.filename)
    save_path = os.path.join(current_app.static_folder, 'videos', filename)
    f.save(save_path)
    return jsonify({'success': True, 'filename': filename})


@admin_bp.route('/laykuchka/videos/delete/<filename>', methods=['POST'])
@admin_required
def delete_video(filename):
    safe = secure_filename(filename)
    fp = os.path.join(current_app.static_folder, 'videos', safe)
    if os.path.exists(fp):
        os.remove(fp)
        return jsonify({'success': True})
    return jsonify({'error': 'Fichier introuvable'}), 404


# ── REPORTS ──
@admin_bp.route('/laykuchka/reports')
@admin_required
def reports():
    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM daily_reports ORDER BY report_date DESC LIMIT 30")
    all_reports = cur.fetchall()
    cur.close()
    return render_template('admin/reports.html', reports=all_reports)
