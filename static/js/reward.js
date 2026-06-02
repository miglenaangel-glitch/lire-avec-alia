function startReward(phrase) {
  // Speak the phrase
  if (phrase) {
    setTimeout(() => {
      const utt = new SpeechSynthesisUtterance(phrase);
      utt.lang = 'fr-FR';
      utt.rate = 0.9;
      speechSynthesis.speak(utt);
    }, 600);
  }

  // Star burst animation
  const emojis = ['⭐', '✨', '🌟', '💫', '🎉', '🎊'];
  for (let i = 0; i < 18; i++) {
    setTimeout(() => spawnStar(emojis[i % emojis.length]), i * 80);
  }

  // Character blink via CSS on the img
  const char = document.getElementById('reward-char');
  if (char) char.style.animation = 'charFloat 2s ease-in-out infinite';
}

function spawnStar(emoji) {
  const el = document.createElement('div');
  el.className = 'star-particle';
  el.textContent = emoji;
  const x = Math.random() * window.innerWidth;
  const y = Math.random() * window.innerHeight;
  const tx = (Math.random() - 0.5) * 200 + 'px';
  const ty = (Math.random() - 0.5) * 200 + 'px';
  el.style.cssText = `left:${x}px;top:${y}px;--tx:${tx};--ty:${ty};`;
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 1300);
}
