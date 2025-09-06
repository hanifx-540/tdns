// copy input text
function copyInput(){
  const txt = document.getElementById('data').value;
  if(!txt) { alert('কোনো Input নেই।'); return; }
  navigator.clipboard.writeText(txt).then(()=> {
    showToast('Input copied to clipboard');
  });
}

// copy encoded text
function copyEncoded(){
  const el = document.getElementById('encodedText');
  if(!el) { alert('কোনো Encoded Output নেই'); return; }
  const text = el.innerText || el.textContent;
  navigator.clipboard.writeText(text).then(()=> {
    showToast('Encoded output copied');
  });
}

// download encoded
function downloadEncoded(){
  const el = document.getElementById('encodedText');
  if(!el) { alert('Nothing to download'); return; }
  const text = el.innerText || el.textContent;
  const blob = new Blob([text], { type: "text/plain;charset=utf-8" });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = "hanifx_encoded.txt";
  document.body.appendChild(a);
  a.click();
  a.remove();
  showToast('Download started');
}

// tiny toast
function showToast(msg){
  const t = document.createElement('div');
  t.textContent = msg;
  t.style.position = 'fixed';
  t.style.right = '20px';
  t.style.bottom = '20px';
  t.style.background = '#111827';
  t.style.color = '#fff';
  t.style.padding = '10px 14px';
  t.style.borderRadius = '8px';
  t.style.boxShadow = '0 6px 20px rgba(0,0,0,0.5)';
  t.style.zIndex = 9999;
  document.body.appendChild(t);
  setTimeout(()=> t.style.opacity = '0', 2200);
  setTimeout(()=> t.remove(), 2600);
}

// small micro-interactions with GSAP (if present)
if (window.gsap) {
  gsap.from(".navbar-brand", { x: -20, opacity: 0, duration: 0.6 });
  gsap.to("#encodeBtn", { y: -2, repeat: -1, yoyo: true, ease: "sine.inOut", duration: 2, delay: 1.2 });
}
