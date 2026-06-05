'use strict';

// ── DATA ──────────────────────────────────────────────────────────────────────

const MOIS = [
  { n:1,  nom:"janvier",   syl:"jan-vi-er",   saison:"hiver",
    apili:[{l:"j",t:"C"},{l:"an",t:"V"},{l:"v",t:"C"},{l:"i",t:"V"},{l:"er",t:"M"}] },
  { n:2,  nom:"février",   syl:"fé-vri-er",   saison:"hiver",
    apili:[{l:"f",t:"C"},{l:"é",t:"V"},{l:"vr",t:"C"},{l:"i",t:"V"},{l:"er",t:"M"}] },
  { n:3,  nom:"mars",      syl:"mars",        saison:"printemps",
    apili:[{l:"m",t:"C"},{l:"a",t:"V"},{l:"r",t:"C"},{l:"s",t:"C"}] },
  { n:4,  nom:"avril",     syl:"a-vril",      saison:"printemps",
    apili:[{l:"a",t:"V"},{l:"vr",t:"C"},{l:"i",t:"V"},{l:"l",t:"M"}] },
  { n:5,  nom:"mai",       syl:"mai",         saison:"printemps",
    apili:[{l:"m",t:"C"},{l:"ai",t:"V"}] },
  { n:6,  nom:"juin",      syl:"juin",        saison:"été",
    apili:[{l:"j",t:"C"},{l:"u",t:"V"},{l:"in",t:"V"}] },
  { n:7,  nom:"juillet",   syl:"juil-let",    saison:"été",
    apili:[{l:"j",t:"C"},{l:"u",t:"V"},{l:"ill",t:"C"},{l:"e",t:"V"},{l:"t",t:"M"}] },
  { n:8,  nom:"août",      syl:"août",        saison:"été",
    apili:[{l:"a",t:"V"},{l:"o",t:"V"},{l:"û",t:"V"},{l:"t",t:"M"}] },
  { n:9,  nom:"septembre", syl:"sep-tem-bre", saison:"automne",
    apili:[{l:"s",t:"C"},{l:"ep",t:"V"},{l:"t",t:"C"},{l:"em",t:"V"},{l:"br",t:"C"},{l:"e",t:"M"}] },
  { n:10, nom:"octobre",   syl:"oc-to-bre",   saison:"automne",
    apili:[{l:"oc",t:"V"},{l:"t",t:"C"},{l:"o",t:"V"},{l:"br",t:"C"},{l:"e",t:"M"}] },
  { n:11, nom:"novembre",  syl:"no-vem-bre",  saison:"automne",
    apili:[{l:"n",t:"C"},{l:"o",t:"V"},{l:"v",t:"C"},{l:"em",t:"V"},{l:"br",t:"C"},{l:"e",t:"M"}] },
  { n:12, nom:"décembre",  syl:"dé-cem-bre",  saison:"hiver",
    apili:[{l:"d",t:"C"},{l:"é",t:"V"},{l:"c",t:"C"},{l:"em",t:"V"},{l:"br",t:"C"},{l:"e",t:"M"}] }
];

const SAISONS = {
  hiver:     { label:"hiver",     icon:"❄",  bg:"#e8f4fc", color:"#1a5276" },
  printemps: { label:"printemps", icon:"🌸", bg:"#edfaf1", color:"#1e8449" },
  été:       { label:"été",       icon:"☀",  bg:"#fef9e7", color:"#9a7d0a" },
  automne:   { label:"automne",   icon:"🍂", bg:"#fef5ec", color:"#a04000" }
};

const COLORS = { C: '#1a3a6b', V: '#c0392b', M: '#b0a090' };

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

function apiliHTML(mois, fontSize) {
  const fs = fontSize || 22;
  return mois.apili
    .map(seg => `<span style="color:${COLORS[seg.t]};font-weight:700;font-size:${fs}px">${seg.l}</span>`)
    .join('');
}

function saisonBadge(saison) {
  const s = SAISONS[saison];
  return `<span class="saison-badge" style="background:${s.bg};color:${s.color}">${s.icon} ${s.label}</span>`;
}

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// ── TAB SWITCHING ─────────────────────────────────────────────────────────────

function switchTab(tab) {
  document.querySelectorAll('.mois-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.mois-panel').forEach(p => p.classList.remove('active'));
  document.querySelector(`.mois-tab[data-tab="${tab}"]`).classList.add('active');
  document.getElementById('panel-' + tab).classList.add('active');
  speechSynthesis.cancel();
  if (tab === 'lecture')  initLecture();
  if (tab === 'ordre')    initOrdre();
  if (tab === 'ecriture') initEcriture();
}

// ── EX1 — LECTURE ─────────────────────────────────────────────────────────────

function initLecture() {
  const grid = document.getElementById('lecture-grid');
  if (grid.dataset.built) return;
  grid.dataset.built = '1';

  MOIS.forEach(m => {
    const card = document.createElement('div');
    card.className = 'mois-card';
    card.dataset.n = m.n;
    card.innerHTML = `
      <div class="card-header">
        <span class="card-num">${m.n}</span>
        ${saisonBadge(m.saison)}
      </div>
      <div class="card-nom">${apiliHTML(m, 22)}</div>
      <div class="card-syl">${m.syl}</div>`;

    let lastTap = 0;
    card.addEventListener('click', () => {
      const now = Date.now();
      const rate = (now - lastTap < 2000) ? 0.6 : 0.7;
      lastTap = now;
      speak(m.nom, rate);
      card.classList.add('played');
      card.style.transform = 'scale(0.95)';
      setTimeout(() => { card.style.transform = ''; }, 120);
    });

    grid.appendChild(card);
  });
}

// ── EX2 — ORDRE ───────────────────────────────────────────────────────────────

let ordreSelected = null;
let ordreSlots = {};
let ordreMois = [];

function initOrdre() {
  ordreMois = shuffle(MOIS).slice(0, 6).sort(() => 0);
  // We need the 6 chosen months in the order they appear in the year (ascending by n)
  // but displayed in shuffled bank — store originals sorted for slot labels
  const sorted = [...ordreMois].sort((a, b) => a.n - b.n);

  ordreSelected = null;
  ordreSlots = {};

  const bank = document.getElementById('ordre-bank');
  const slotsEl = document.getElementById('ordre-slots');
  const feedback = document.getElementById('ordre-feedback');

  bank.innerHTML = '';
  slotsEl.innerHTML = '';
  feedback.textContent = '';

  // Slots — numbered by relative position (1–6) but expect a specific mois
  sorted.forEach((m, i) => {
    const slot = document.createElement('div');
    slot.className = 'ordre-slot';
    slot.dataset.expect = m.n;
    slot.dataset.pos = i + 1;
    slot.innerHTML = `<span class="slot-label">${i + 1}</span>`;
    slot.addEventListener('click', () => placeInSlot(slot));
    slotsEl.appendChild(slot);
    ordreSlots[m.n] = slot;
  });

  // Bank — shuffled
  const shuffledBank = shuffle(ordreMois);
  shuffledBank.forEach(m => {
    const tile = document.createElement('div');
    tile.className = 'ordre-tile';
    tile.dataset.n = m.n;
    tile.innerHTML = apiliHTML(m, 20);
    tile.addEventListener('click', () => selectOrdreTile(tile, m));
    bank.appendChild(tile);
  });
}

function selectOrdreTile(tile, m) {
  if (tile.dataset.placed) return;
  // Toggle deselect
  if (ordreSelected && ordreSelected.tile === tile) {
    tile.classList.remove('selected');
    ordreSelected = null;
    return;
  }
  document.querySelectorAll('.ordre-tile.selected').forEach(t => t.classList.remove('selected'));
  tile.classList.add('selected');
  ordreSelected = { tile, m };
  speak(m.nom, 0.7);
}

function placeInSlot(slot) {
  if (!ordreSelected) return;
  const { tile, m } = ordreSelected;

  // Remove previous occupant from this slot if any
  const prevN = slot.dataset.placed;
  if (prevN) {
    const prevTile = document.querySelector(`.ordre-tile[data-n="${prevN}"]`);
    if (prevTile) { delete prevTile.dataset.placed; prevTile.style.opacity = '1'; }
  }

  slot.dataset.placed = m.n;
  slot.innerHTML = `<span class="slot-label">${slot.dataset.pos}</span>${apiliHTML(m, 18)}`;
  slot.classList.remove('correct', 'wrong');

  tile.dataset.placed = '1';
  tile.style.opacity = '0.35';
  tile.classList.remove('selected');
  ordreSelected = null;
}

function verifierOrdre() {
  let correct = 0;
  document.querySelectorAll('.ordre-slot').forEach(slot => {
    const placed = parseInt(slot.dataset.placed || '0');
    const expect = parseInt(slot.dataset.expect);
    if (placed === expect) {
      slot.classList.add('correct');
      slot.classList.remove('wrong');
      correct++;
    } else if (placed) {
      slot.classList.add('wrong');
      slot.classList.remove('correct');
    }
  });

  const feedback = document.getElementById('ordre-feedback');
  const total = ordreMois.length;
  if (correct === total) {
    feedback.textContent = 'Parfait Alia ! Tu connais l\'ordre des mois !';
    feedback.className = 'ordre-feedback success';
    speak('Parfait Alia ! Tu connais l\'ordre des mois !', 0.7);
  } else {
    feedback.textContent = `${correct} mois sur ${total} au bon endroit !`;
    feedback.className = 'ordre-feedback partial';
  }
}

// ── EX3 — ÉCRITURE ────────────────────────────────────────────────────────────

let ecritureQueue = [];
let ecritureIdx = 0;
let ecriturePlaced = [];
let ecritureTiles = [];
let ecritureScore = 0;

const DISTRACTEURS = ['a','e','i','o','u','r','s','t','n','l','m','p','c','d','b','f'];

function initEcriture() {
  ecritureQueue = shuffle([...MOIS]);
  ecritureIdx = 0;
  ecritureScore = 0;
  renderEcritureDots();
  showEcritureMois();
}

function renderEcritureDots() {
  const dots = document.getElementById('ecriture-dots');
  dots.innerHTML = '';
  ecritureQueue.forEach((m, i) => {
    const d = document.createElement('span');
    d.className = 'ecriture-dot' + (i === ecritureIdx ? ' current' : (i < ecritureIdx ? ' done' : ''));
    dots.appendChild(d);
  });
}

function showEcritureMois() {
  if (ecritureIdx >= ecritureQueue.length) {
    showEcritureEnd();
    return;
  }
  renderEcritureDots();
  const m = ecritureQueue[ecritureIdx];
  const s = SAISONS[m.saison];

  document.getElementById('ecriture-num').textContent = m.n;
  document.getElementById('ecriture-badge').innerHTML = saisonBadge(m.saison);
  document.getElementById('ecriture-feedback').textContent = '';
  document.getElementById('ecriture-feedback').className = 'ecriture-feedback';

  // Answer slots
  const slots = document.getElementById('ecriture-slots');
  slots.innerHTML = '';
  ecriturePlaced = Array(m.nom.length).fill(null);
  for (let i = 0; i < m.nom.length; i++) {
    const sl = document.createElement('div');
    sl.className = 'ecriture-slot';
    sl.dataset.idx = i;
    sl.addEventListener('click', () => removeLetter(i));
    slots.appendChild(sl);
  }

  // Tiles: letters + distractors
  const letters = m.nom.split('');
  const needed = Math.min(4, Math.max(2, Math.floor(m.nom.length * 0.4)));
  const pool = [...DISTRACTEURS].filter(l => !letters.includes(l));
  const extras = shuffle(pool).slice(0, needed);
  const allTiles = shuffle([...letters, ...extras]);

  const tilesEl = document.getElementById('ecriture-tiles');
  tilesEl.innerHTML = '';
  ecritureTiles = allTiles;
  allTiles.forEach(letter => {
    const tile = document.createElement('button');
    const isVowel = 'aeiouyàáâãäåèéêëìíîïòóôõöùúûü'.includes(letter.toLowerCase());
    tile.className = 'ecriture-tile';
    tile.style.background = isVowel ? '#c0392b' : '#1a3a6b';
    tile.textContent = letter;
    tile.addEventListener('click', () => addLetter(letter, tile));
    tilesEl.appendChild(tile);
  });
}

function addLetter(letter, tile) {
  const nextIdx = ecriturePlaced.indexOf(null);
  if (nextIdx === -1) return;
  ecriturePlaced[nextIdx] = letter;
  tile.disabled = true;
  tile.style.opacity = '0.35';

  const slot = document.querySelector(`.ecriture-slot[data-idx="${nextIdx}"]`);
  const isVowel = 'aeiouyàáâãäåèéêëìíîïòóôõöùúûü'.includes(letter.toLowerCase());
  slot.textContent = letter;
  slot.style.color = isVowel ? '#c0392b' : '#1a3a6b';
  slot.dataset.letter = letter;
}

function removeLetter(idx) {
  if (ecriturePlaced[idx] === null) return;
  const letter = ecriturePlaced[idx];
  ecriturePlaced[idx] = null;

  const slot = document.querySelector(`.ecriture-slot[data-idx="${idx}"]`);
  slot.textContent = '';
  slot.style.color = '';
  delete slot.dataset.letter;

  // Re-enable the matching tile
  const tiles = document.querySelectorAll('.ecriture-tile');
  for (const t of tiles) {
    if (t.disabled && t.textContent === letter) {
      t.disabled = false;
      t.style.opacity = '1';
      break;
    }
  }
}

function effacerDerniere() {
  for (let i = ecriturePlaced.length - 1; i >= 0; i--) {
    if (ecriturePlaced[i] !== null) {
      removeLetter(i);
      break;
    }
  }
}

function verifierEcriture() {
  const m = ecritureQueue[ecritureIdx];
  const answer = ecriturePlaced.join('');
  const feedback = document.getElementById('ecriture-feedback');

  if (answer === m.nom) {
    ecritureScore++;
    feedback.textContent = `Bravo Alia ! C'est ${m.nom} !`;
    feedback.className = 'ecriture-feedback success';
    speak(`Bravo Alia ! C'est ${m.nom} !`, 0.7);
    recordProgress(m.nom, true);
    ecritureIdx++;
    setTimeout(showEcritureMois, 1500);
  } else {
    feedback.textContent = `Pas tout à fait — le mois ${m.n}, c'est ${m.nom}`;
    feedback.className = 'ecriture-feedback partial';
    speak(m.nom, 0.6);
    recordProgress(m.nom, false);
    ecritureIdx++;
    setTimeout(showEcritureMois, 2200);
  }
}

function showEcritureEnd() {
  const panel = document.getElementById('panel-ecriture');
  panel.innerHTML = `
    <div style="text-align:center;padding:2rem;">
      <div style="font-size:3rem;margin-bottom:1rem;">🎉</div>
      <div style="font-size:1.4rem;font-weight:800;color:#1a3a6b;margin-bottom:0.5rem;">
        ${ecritureScore} / 12 du premier coup !
      </div>
      <button class="mois-btn" onclick="initEcriture()" style="margin-top:1.5rem;">
        Recommencer
      </button>
    </div>`;
  speak(`${ecritureScore} sur 12 du premier coup !`, 0.7);
}

function recordProgress(nom, correct) {
  fetch('/api/record', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ element_type: 'mois_ecriture', element_value: nom, correct })
  }).catch(() => {});
}

// ── INIT ──────────────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
  speechSynthesis.getVoices();
  if (speechSynthesis.onvoiceschanged !== undefined) {
    speechSynthesis.onvoiceschanged = () => speechSynthesis.getVoices();
  }

  document.querySelectorAll('.mois-tab').forEach(t => {
    t.addEventListener('click', () => switchTab(t.dataset.tab));
  });

  // Activate initial tab
  const active = document.querySelector('.mois-tab.active');
  if (active) {
    const tab = active.dataset.tab;
    if (tab === 'lecture')  initLecture();
    if (tab === 'ordre')    initOrdre();
    if (tab === 'ecriture') initEcriture();
  }
});
