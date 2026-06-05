'use strict';

// ── DATA ──────────────────────────────────────────────────────────────────────

const HEURES = [
  { n:1,  label:"une heure",    tts:"Il est une heure.",    h:1,  midi:false, minuit:false, personnage:"skye" },
  { n:2,  label:"deux heures",  tts:"Il est deux heures.",  h:2,  midi:false, minuit:false, personnage:"skye" },
  { n:3,  label:"trois heures", tts:"Il est trois heures.", h:3,  midi:false, minuit:false, personnage:"skye" },
  { n:4,  label:"quatre heures",tts:"Il est quatre heures.",h:4,  midi:false, minuit:false, personnage:"skye" },
  { n:5,  label:"cinq heures",  tts:"Il est cinq heures.",  h:5,  midi:false, minuit:false, personnage:"skye" },
  { n:6,  label:"six heures",   tts:"Il est six heures.",   h:6,  midi:false, minuit:false, personnage:"skye" },
  { n:7,  label:"sept heures",  tts:"Il est sept heures.",  h:7,  midi:false, minuit:false, personnage:"skye" },
  { n:8,  label:"huit heures",  tts:"Il est huit heures.",  h:8,  midi:false, minuit:false, personnage:"skye" },
  { n:9,  label:"neuf heures",  tts:"Il est neuf heures.",  h:9,  midi:false, minuit:false, personnage:"skye" },
  { n:10, label:"dix heures",   tts:"Il est dix heures.",   h:10, midi:false, minuit:false, personnage:"skye" },
  { n:11, label:"onze heures",  tts:"Il est onze heures.",  h:11, midi:false, minuit:false, personnage:"skye" },
  { n:12, label:"midi",         tts:"Il est midi.",         h:12, midi:true,  minuit:false, personnage:"skye" },
  { n:0,  label:"minuit",       tts:"Il est minuit.",       h:0,  midi:false, minuit:true,  personnage:"lumi" }
];

const PERSONNAGE_THEME = {
  skye: { bg:"#fffbf0", accent:"#f0b429", label:"Skye 🦄", emoji:"🦄" },
  lumi: { bg:"#f5f0ff", accent:"#9b59b6", label:"Lumi 🦊", emoji:"🦊" }
};

// ── UTILITIES ─────────────────────────────────────────────────────────────────

function speak(text, rate = 0.7) {
  if (!window.speechSynthesis) return;
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'fr-FR';
  u.rate = rate;
  u.pitch = 1.05;
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

// Build Apili-colored HTML for a label string
// Simple rule: vowels=red, consonants=blue, silent endings=grey
const VOWELS = new Set('aeiouyéèêëàâîïôùûü');
const SILENT_ENDINGS = /([rsx])$/; // simplified for heure labels

function apiliLabel(text) {
  return text.split('').map(ch => {
    if (ch === ' ') return ' ';
    const lc = ch.toLowerCase();
    const isVowel = VOWELS.has(lc);
    // simple mute detection: trailing s on heures
    const color = isVowel ? '#c0392b' : '#1a3a6b';
    return `<span style="color:${color};font-weight:700">${ch}</span>`;
  }).join('');
}

function personnageBadge(p) {
  const t = PERSONNAGE_THEME[p];
  return `<span class="personnage-badge">${t.emoji}</span>`;
}

function heureDisplay(h) {
  if (h.minuit) return `<span class="heure-minuit-badge">minuit ✦</span>`;
  if (h.midi)   return `<span class="heure-midi-badge">midi ✦</span>`;
  const pad = String(h.h).padStart(2, '0');
  return `${pad}:00`;
}

function recordProgress(label, correct) {
  fetch('/api/record', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ element_type: 'heure_exacte', element_value: label, correct })
  }).catch(() => {});
}

// ── TAB SWITCHING ─────────────────────────────────────────────────────────────

function switchTab(tab) {
  document.querySelectorAll('.heure-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.heure-panel').forEach(p => p.classList.remove('active'));
  document.querySelector(`.heure-tab[data-tab="${tab}"]`).classList.add('active');
  document.getElementById('panel-' + tab).classList.add('active');
  speechSynthesis.cancel();
  if (tab === 'match')   initMatch();
  if (tab === 'parle')   initParle();
  if (tab === 'skyLumi') initSkyLumi();
}

// ── EX1 — HEURE MATCH ────────────────────────────────────────────────────────

let matchQuestion = null;
let matchAnswered = false;

function initMatch() {
  matchAnswered = false;
  matchQuestion = generateQuestion();
  renderMatch();
}

function generateQuestion() {
  const correct = HEURES[Math.floor(Math.random() * HEURES.length)];
  const pool = HEURES.filter(h => h !== correct);
  const wrong = shuffle(pool).slice(0, 2);
  return { correct, choices: shuffle([correct, ...wrong]) };
}

function renderMatch() {
  const { correct, choices } = matchQuestion;
  const theme = PERSONNAGE_THEME[correct.personnage];

  const panel = document.getElementById('panel-match');
  panel.style.background = theme.bg;

  document.getElementById('match-display').innerHTML = heureDisplay(correct);
  document.getElementById('match-perso').innerHTML = '';
  document.getElementById('match-feedback').textContent = '';
  document.getElementById('match-feedback').className = 'heure-feedback';

  const choicesEl = document.getElementById('match-choices');
  choicesEl.innerHTML = '';
  choices.forEach(h => {
    const btn = document.createElement('button');
    btn.className = 'heure-choice-btn';
    btn.innerHTML = apiliLabel(h.label);
    if (h.midi)   btn.innerHTML += ' <span class="heure-midi-badge" style="font-size:11px">midi</span>';
    if (h.minuit) btn.innerHTML += ' <span class="heure-minuit-badge" style="font-size:11px">minuit</span>';
    btn.addEventListener('click', () => answerMatch(h, btn));
    choicesEl.appendChild(btn);
  });
}

function answerMatch(h, btn) {
  if (matchAnswered) return;
  matchAnswered = true;

  const { correct } = matchQuestion;
  const isCorrect = h.n === correct.n;
  const feedback = document.getElementById('match-feedback');
  const perso = document.getElementById('match-perso');

  btn.style.transform = 'scale(0.95)';
  setTimeout(() => { btn.style.transform = ''; }, 120);

  if (isCorrect) {
    btn.classList.add('correct');
    feedback.textContent = 'Bravo Alia !';
    feedback.className = 'heure-feedback success';
    perso.textContent = PERSONNAGE_THEME[correct.personnage].emoji;
    speak(correct.tts, 0.7);
    recordProgress(correct.label, true);
    setTimeout(initMatch, 2000);
  } else {
    btn.classList.add('wrong');
    feedback.textContent = `Pas tout à fait — écoute !`;
    feedback.className = 'heure-feedback partial';
    speak(correct.tts, 0.7);
    recordProgress(h.label, false);
    // Highlight correct
    document.querySelectorAll('.heure-choice-btn').forEach(b => {
      if (b.textContent.includes(correct.label)) b.classList.add('correct');
    });
    setTimeout(initMatch, 2500);
  }
}

// ── EX2 — QUI PARLE ──────────────────────────────────────────────────────────

let parleQueue = [];
let parleIdx = 0;

function initParle() {
  parleQueue = shuffle([...HEURES]);
  parleIdx = 0;
  renderParle();
}

function renderParle() {
  if (parleIdx >= parleQueue.length) {
    document.getElementById('panel-parle').innerHTML = `
      <div style="text-align:center;padding:3rem 1rem;">
        <div style="font-size:3rem;">🐶</div>
        <div style="font-size:1.3rem;font-weight:800;color:#1a3a6b;margin-top:1rem;">
          Tu connais toutes les heures !
        </div>
        <button class="heure-btn" onclick="initParle()" style="margin-top:1.5rem;">
          Recommencer
        </button>
      </div>`;
    speak("Tu connais toutes les heures !", 0.7);
    return;
  }

  const h = parleQueue[parleIdx];
  const theme = PERSONNAGE_THEME[h.personnage];
  const panel = document.getElementById('panel-parle');
  panel.style.background = theme.bg;

  document.getElementById('parle-display').innerHTML = heureDisplay(h);
  document.getElementById('parle-feedback').textContent = '';
  document.getElementById('parle-feedback').className = 'heure-feedback';
  document.getElementById('parle-btn').disabled = false;
  document.getElementById('parle-btn').textContent = "J'ai dit !";

  // Choco prompt
  document.getElementById('parle-choco').innerHTML =
    `<span style="font-size:1.5rem;">🐶</span>
     <span style="font-size:1rem;color:#555;">Il est quelle heure ?</span>`;
}

function parleConfirm() {
  const h = parleQueue[parleIdx];
  const feedback = document.getElementById('parle-feedback');
  document.getElementById('parle-btn').disabled = true;
  document.getElementById('parle-btn').textContent = '✓';

  feedback.textContent = h.tts;
  feedback.className = 'heure-feedback success';
  speak(h.tts, 0.7);

  parleIdx++;
  setTimeout(renderParle, 1800);
}

// ── EX3 — SKYE OU LUMI ───────────────────────────────────────────────────────

let skylumiQueue = [];
let skylumiIdx = 0;
let skylumiScore = 0;

function initSkyLumi() {
  skylumiQueue = shuffle([...HEURES]);
  skylumiIdx = 0;
  skylumiScore = 0;
  renderSkyLumi();
}

function renderSkyLumi() {
  if (skylumiIdx >= skylumiQueue.length) {
    document.getElementById('panel-skyLumi').innerHTML = `
      <div style="text-align:center;padding:3rem 1rem;">
        <div style="font-size:2.5rem;">🦄🦊</div>
        <div style="font-size:1.3rem;font-weight:800;color:#1a3a6b;margin-top:1rem;">
          ${skylumiScore} / ${skylumiQueue.length} !
        </div>
        <button class="heure-btn" onclick="initSkyLumi()" style="margin-top:1.5rem;">
          Recommencer
        </button>
      </div>`;
    speak(`${skylumiScore} sur ${skylumiQueue.length} !`, 0.7);
    return;
  }

  const h = skylumiQueue[skylumiIdx];
  document.getElementById('skylumi-display').innerHTML = heureDisplay(h);
  document.getElementById('skylumi-feedback').textContent = '';
  document.getElementById('skylumi-feedback').className = 'heure-feedback';
  document.getElementById('skylumi-score').textContent =
    `${skylumiIdx} / ${skylumiQueue.length}`;

  // Enable buttons
  document.querySelectorAll('.skylumi-btn').forEach(b => {
    b.disabled = false;
    b.classList.remove('correct', 'wrong');
  });
}

function answerSkyLumi(choice) {
  const h = skylumiQueue[skylumiIdx];
  const isCorrect = choice === h.personnage;
  const feedback = document.getElementById('skylumi-feedback');
  const theme = PERSONNAGE_THEME[h.personnage];

  document.querySelectorAll('.skylumi-btn').forEach(b => b.disabled = true);

  if (isCorrect) {
    feedback.textContent = `${theme.emoji} ${theme.label} — Bravo !`;
    feedback.className = 'heure-feedback success';
    skylumiScore++;
    speak(h.tts, 0.7);
  } else {
    const correct = PERSONNAGE_THEME[h.personnage];
    feedback.textContent = `C'est ${correct.label} — ${h.tts}`;
    feedback.className = 'heure-feedback partial';
    speak(h.tts, 0.7);
    // highlight correct button
    document.querySelectorAll('.skylumi-btn').forEach(b => {
      if (b.dataset.choice === h.personnage) b.classList.add('correct');
    });
  }

  skylumiIdx++;
  setTimeout(renderSkyLumi, 1800);
}

// ── INIT ──────────────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
  speechSynthesis.getVoices();
  if (speechSynthesis.onvoiceschanged !== undefined) {
    speechSynthesis.onvoiceschanged = () => speechSynthesis.getVoices();
  }

  document.querySelectorAll('.heure-tab').forEach(t => {
    t.addEventListener('click', () => switchTab(t.dataset.tab));
  });

  const active = document.querySelector('.heure-tab.active');
  if (active) {
    const tab = active.dataset.tab;
    if (tab === 'match')   initMatch();
    if (tab === 'parle')   initParle();
    if (tab === 'skyLumi') initSkyLumi();
  }
});
