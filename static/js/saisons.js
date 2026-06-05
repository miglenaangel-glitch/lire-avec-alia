'use strict';

// ── DATA ──────────────────────────────────────────────────────────────────────

const SAISONS_DATA = {
  hiver: {
    label: "Hiver", icon: "❄", bg: "#e8f4fc", color: "#1a5276",
    mois: [12, 1, 2],
    fetes: [
      { date: "25/12", label: "Noël 🎄",           type: "officiel" },
      { date: "31/12", label: "Saint-Sylvestre 🥂", type: "officiel" },
      { date: "01/01", label: "Jour de l'An 🎆",   type: "officiel" }
    ],
    anniversaires: [
      { date: "09/01", label: "Adri (maman) 🌟",  prenom: "Adri",   lien: "maman" },
      { date: "09/01", label: "Titi (tata) 🌟",   prenom: "Titi",   lien: "tata" },
      { date: "26/02", label: "Victor 🎂",         prenom: "Victor", lien: "cousin" }
    ],
    vacances: ["Vacances de Noël (~25 déc)", "Vacances d'Hiver (~fév)"]
  },
  printemps: {
    label: "Printemps", icon: "🌸", bg: "#edfaf1", color: "#1e8449",
    mois: [3, 4, 5],
    fetes: [
      { date: "variable", label: "Pâques 🐣",          type: "officiel" },
      { date: "01/05",    label: "Fête du Travail 🌺", type: "officiel" },
      { date: "08/05",    label: "Victoire 1945 🕊",   type: "officiel" }
    ],
    anniversaires: [
      { date: "28/04", label: "Naïden 🎂",    prenom: "Naïden",   lien: "cousin" },
      { date: "20/05", label: "Baba Fiy 👵",  prenom: "Baba Fiy", lien: "mamie" },
      { date: "21/05", label: "Ile tonton 🎂",prenom: "Ile",      lien: "tonton" }
    ],
    vacances: ["Vacances de Printemps (~Pâques)"]
  },
  ete: {
    label: "Été", icon: "☀", bg: "#fef9e7", color: "#9a7d0a",
    mois: [6, 7, 8],
    fetes: [
      { date: "03/06", label: "Bonibon fête ses années 🎧", type: "special" },
      { date: "14/07", label: "Fête Nationale 🎆",          type: "officiel" },
      { date: "15/08", label: "Assomption ☀",               type: "officiel" }
    ],
    anniversaires: [
      { date: "21/07", label: "ALIA 🌟🎉",  prenom: "Alia",  lien: "moi",     special: true },
      { date: "01/08", label: "Maxi 🎂",    prenom: "Maxi",  lien: "cousin" },
      { date: "22/08", label: "Marsi 🎂",   prenom: "Marsi", lien: "cousine" }
    ],
    vacances: ["Grandes Vacances 🎉 (juillet + août — ~8 semaines !)"]
  },
  automne: {
    label: "Automne", icon: "🍂", bg: "#fef5ec", color: "#a04000",
    mois: [9, 10, 11],
    fetes: [
      { date: "~01/09", label: "La Rentrée 📚",  type: "scolaire" },
      { date: "31/10",  label: "Halloween 🎃",   type: "special" },
      { date: "01/11",  label: "Toussaint 🕯",   type: "officiel" },
      { date: "11/11",  label: "Armistice 🕊",   type: "officiel" }
    ],
    anniversaires: [
      { date: "06/10", label: "Daymian 🎂", prenom: "Daymian", lien: "cousin" }
    ],
    vacances: ["Vacances de la Toussaint (~nov)"]
  }
};

// Mois names (mirrors MOIS from mois.js — indexed by n)
const MOIS_NOMS = {
  1:"janvier", 2:"février", 3:"mars", 4:"avril", 5:"mai", 6:"juin",
  7:"juillet", 8:"août", 9:"septembre", 10:"octobre", 11:"novembre", 12:"décembre"
};

// Saison key for each month number
const MOIS_SAISON = {};
Object.entries(SAISONS_DATA).forEach(([key, s]) => {
  s.mois.forEach(n => { MOIS_SAISON[n] = key; });
});

// ── UTILITIES ─────────────────────────────────────────────────────────────────

function speak(text, rate = 0.7) {
  if (!window.speechSynthesis) return;
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'fr-FR'; u.rate = rate; u.pitch = 1.05;
  speechSynthesis.speak(u);
}

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// Apili coloring for a month name using MOIS data (from mois.js)
function apiliMoisHTML(n, fontSize) {
  if (typeof MOIS === 'undefined') {
    // fallback if mois.js not loaded
    return `<span style="font-weight:700;font-size:${fontSize||22}px">${MOIS_NOMS[n]}</span>`;
  }
  const m = MOIS.find(m => m.n === n);
  if (!m) return MOIS_NOMS[n];
  return apiliHTML(m, fontSize || 22);
}

// ── TAB SWITCHING ─────────────────────────────────────────────────────────────

function switchSaisonTab(key) {
  document.querySelectorAll('.saison-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.saison-panel').forEach(p => p.classList.remove('active'));
  const tab = document.querySelector(`.saison-tab[data-saison="${key}"]`);
  const panel = document.getElementById('panel-' + key);
  if (tab) tab.classList.add('active');
  if (panel) panel.classList.add('active');
  speechSynthesis.cancel();
}

function switchExTab(tab) {
  document.querySelectorAll('.ex-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.ex-panel').forEach(p => p.classList.remove('active'));
  document.querySelector(`.ex-tab[data-ex="${tab}"]`).classList.add('active');
  document.getElementById('expanel-' + tab).classList.add('active');
  if (tab === 'match')   initMatch();
  if (tab === 'calendrier') initCalendrier();
}

// ── BUILD SAISON PANELS ───────────────────────────────────────────────────────

function buildSaisonPanels() {
  Object.entries(SAISONS_DATA).forEach(([key, s]) => {
    const panel = document.getElementById('panel-' + key);
    if (!panel) return;

    // Header
    let html = `<div class="saison-panel-header" style="background:${s.bg};color:${s.color}">
      <span class="saison-big-icon">${s.icon}</span>
      <span class="saison-big-label">${s.label}</span>
    </div>`;

    // Months
    html += `<div class="saison-section">
      <div class="saison-section-title">Les mois</div>
      <div class="saison-mois-row">`;
    s.mois.forEach(n => {
      html += `<div class="saison-mois-card" style="background:${s.bg};border-color:${s.color}20"
        onclick="speak('${MOIS_NOMS[n]}', 0.7)">
        <span class="saison-mois-num">${n}</span>
        <div class="saison-mois-nom">${apiliMoisHTML(n, 20)}</div>
      </div>`;
    });
    html += `</div></div>`;

    // Fêtes
    html += `<div class="saison-section">
      <div class="saison-section-title">Les fêtes</div>`;
    s.fetes.forEach(f => {
      const isHalloween = f.label.includes('Halloween');
      const isBonibon  = f.label.includes('Bonibon');
      let cls = 'saison-fete-row';
      let extra = '';
      if (isHalloween) {
        cls += ' halloween';
        extra = `<span class="saison-fete-note">la fête préférée d'Alia !</span>`;
      }
      if (isBonibon) cls += ' bonibon';
      html += `<div class="${cls}">
        <span class="saison-fete-date">${f.date}</span>
        <span class="saison-fete-label">${f.label}</span>
        ${extra}
      </div>`;
    });
    html += `</div>`;

    // Anniversaires
    html += `<div class="saison-section">
      <div class="saison-section-title">Les anniversaires 🎂</div>`;
    s.anniversaires.forEach(a => {
      if (a.special) {
        html += `<div class="anniversaire-special">
          <span class="star-anim">🌟</span>
          <span style="color:#1a3a6b;font-weight:700">${a.date}</span>
          <span style="color:black"> — </span>
          <span style="color:#c0392b;font-weight:700">C'est toi, Alia !</span>
          <span class="star-anim">🎉</span>
        </div>`;
      } else if (a.lien === 'maman') {
        html += `<div class="anniversaire-bonibon">
          <span>🌟</span>
          <span style="color:black">${a.date} — ${a.prenom}</span>
        </div>`;
      } else {
        html += `<div class="saison-anniv-row">
          <span class="saison-fete-date">${a.date}</span>
          <span style="color:black">${a.label}</span>
        </div>`;
      }
    });
    html += `</div>`;

    // Vacances
    if (s.vacances && s.vacances.length) {
      html += `<div class="saison-section">
        <div class="saison-section-title">Les vacances 📚</div>`;
      s.vacances.forEach(v => {
        html += `<div class="saison-vacance-row">📚 ${v}</div>`;
      });
      html += `</div>`;
    }

    panel.innerHTML = html;
  });
}

// ── EX1 — SAISON MATCH ───────────────────────────────────────────────────────

let matchMois = null;
let matchAnswered = false;

function initMatch() {
  matchAnswered = false;
  // Pick random month
  const allN = [1,2,3,4,5,6,7,8,9,10,11,12];
  const n = allN[Math.floor(Math.random() * 12)];
  matchMois = n;

  const nom = MOIS_NOMS[n];
  document.getElementById('match-mois').innerHTML = apiliMoisHTML(n, 26);
  document.getElementById('match-feedback').textContent = '';
  document.getElementById('match-feedback').className = 'saison-feedback';

  const btns = document.querySelectorAll('.match-saison-btn');
  btns.forEach(b => {
    b.disabled = false;
    b.classList.remove('correct', 'wrong');
    b.style.opacity = '1';
  });
}

function answerMatch(key) {
  if (matchAnswered) return;
  matchAnswered = true;

  const correct = MOIS_SAISON[matchMois];
  const s = SAISONS_DATA[correct];
  const feedback = document.getElementById('match-feedback');
  const btn = document.querySelector(`.match-saison-btn[data-saison="${key}"]`);

  btn.style.transform = 'scale(0.95)';
  setTimeout(() => { btn.style.transform = ''; }, 120);

  document.querySelectorAll('.match-saison-btn').forEach(b => b.disabled = true);

  if (key === correct) {
    btn.classList.add('correct');
    feedback.textContent = `Bravo ! ${MOIS_NOMS[matchMois]} est en ${s.label} ${s.icon}`;
    feedback.className = 'saison-feedback success';
    speak(`${MOIS_NOMS[matchMois]} est en ${s.label}`, 0.7);
  } else {
    btn.classList.add('wrong');
    const correctBtn = document.querySelector(`.match-saison-btn[data-saison="${correct}"]`);
    if (correctBtn) correctBtn.classList.add('correct');
    feedback.textContent = `Pas tout à fait ! ${MOIS_NOMS[matchMois]} est en ${s.label} ${s.icon}`;
    feedback.className = 'saison-feedback partial';
    speak(`${MOIS_NOMS[matchMois]} est en ${s.label}`, 0.7);
  }

  setTimeout(initMatch, 2200);
}

// ── EX2 — CALENDRIER VIVANT ───────────────────────────────────────────────────

function initCalendrier() {
  const grid = document.getElementById('calendrier-grid');
  if (grid.dataset.built) return;
  grid.dataset.built = '1';

  // Build all 12 months in order
  for (let n = 1; n <= 12; n++) {
    const sKey = MOIS_SAISON[n];
    const s = SAISONS_DATA[sKey];
    const nom = MOIS_NOMS[n];

    // Collect events for this month
    const events = [];
    s.fetes.forEach(f => {
      const m = f.date.match(/\/(\d{2})$/);
      if (m && parseInt(m[1]) === n) events.push(f);
      if (f.date === 'variable' && (n === 3 || n === 4)) events.push(f);
      if (f.date.startsWith('~') && f.date.includes('/0' + n) ) events.push(f);
      // Rentrée in September
      if (f.label.includes('Rentrée') && n === 9) events.push(f);
    });
    s.anniversaires.forEach(a => {
      const m = a.date.match(/\/(\d{2})$/);
      if (m && parseInt(m[1]) === n) events.push({ ...a, isAnniv: true });
    });

    const card = document.createElement('div');
    card.className = 'cal-card';
    card.style.borderColor = s.color + '60';
    card.style.background = s.bg;

    let evHtml = '';
    events.forEach(ev => {
      if (ev.isAnniv) {
        if (ev.special) {
          evHtml += `<div class="cal-ev special">🌟 <span style="color:#c0392b;font-weight:700">C'est toi, Alia !</span></div>`;
        } else if (ev.label.includes('Bonibon')) {
          evHtml += `<div class="cal-ev bonibon">🎧 <span style="color:black">${ev.prenom}</span></div>`;
        } else {
          evHtml += `<div class="cal-ev anniv">🎂 <span style="color:black">${ev.prenom || ev.label}</span></div>`;
        }
      } else if (ev.label.includes('Halloween')) {
        evHtml += `<div class="cal-ev halloween">🎃 <span style="color:black">Halloween !</span></div>`;
      } else {
        evHtml += `<div class="cal-ev fete">${ev.label}</div>`;
      }
    });

    card.innerHTML = `
      <div class="cal-card-header" style="color:${s.color}">
        <span class="cal-num">${n}</span>
        <span class="cal-nom">${apiliMoisHTML(n, 16)}</span>
        <span class="cal-saison-icon">${s.icon}</span>
      </div>
      <div class="cal-events">${evHtml || ''}</div>`;

    card.addEventListener('click', () => {
      speak(nom, 0.7);
      card.classList.toggle('expanded');
    });

    grid.appendChild(card);
  }
}

// ── INIT ──────────────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
  speechSynthesis.getVoices();
  if (speechSynthesis.onvoiceschanged !== undefined) {
    speechSynthesis.onvoiceschanged = () => speechSynthesis.getVoices();
  }

  buildSaisonPanels();

  document.querySelectorAll('.saison-tab').forEach(t => {
    t.addEventListener('click', () => switchSaisonTab(t.dataset.saison));
  });

  document.querySelectorAll('.ex-tab').forEach(t => {
    t.addEventListener('click', () => switchExTab(t.dataset.ex));
  });

  // Init active ex tab
  const activeEx = document.querySelector('.ex-tab.active');
  if (activeEx) {
    const ex = activeEx.dataset.ex;
    if (ex === 'match')      initMatch();
    if (ex === 'calendrier') initCalendrier();
  }
});
