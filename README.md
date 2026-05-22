# 🤖 Boss Toggle Lock... (With TAB Toggle)

Ek super fun aur interactive command-line password protector bot! Yeh bot na sirf tumhari terminal ko secure karta hai, balki galat password daalne par maze bhi leta hai aur bol kar jawab deta hai.

---

## ✨ Features (Isme kya khass hai?)

- **🎙️ Talking Bot:** `pyttsx3` library ka use karke bot real-time me aapse baatein karta hai.
- **🔄 TAB Key Magic:** Type karte waqt keyboard ka `TAB` button dabaoge, toh password turant chhip jayega (`*`) ya dikhne lagega.
- **🎭 Funny Roasts & Easter Eggs:** Agar password me `Tony Stark` likhoge toh alag response aayega, aur galat password par bot gusse me react karega!
- **🛑 Auto-Block:** 3 baar galat password daalne par bot system lock karne ka naatak karke exit ho jata hai.

---

## 📚 Libraries Used (Kaun si library kya kaam kar rahi hai?)

Is project me humne Python ki 4 libraries ka use kiya hai, jisme se kuch built-in (pehle se aati hain) hain:

1. **`pyttsx3` (External Library):**
   - **Kaam:** Yeh Text-to-Speech (TTS) engine hai. Jo bhi text hum script me likhte hain, yeh use laptop ke speaker se bol kar sunata hai.
2. **`msvcrt` (Built-in - Only for Windows):**
   - **Kaam:** Iska full form hai *Microsoft Visual C Runtime*. Iska `msvcrt.getch()` function keyboard ki keys ko hawa me hi catch kar leta hai bina `Enter` dabaye, jisse hum `TAB` aur `Backspace` ko track kar paate hain.
3. **`sys` (Built-in):**
   - **Kaam:** Iska `sys.stdout.write()` terminal ki single line ko mitaane aur naya data print karne ke liye use hota hai (isi se TAB dabane par text live change hota hai).
4. **`time` (Built-in):**
   - **Kaam:** Self-destruct wale scene me 1 second ka delay (pausa) dene ke liye use kiya hai.

---

## 🚀 Step-by-Step Guide: Kaise use karein?

Apne computer par is bot ko chalane ke liye niche diye gaye steps follow karo:

### Step 1: External Library Install Karein
Sabse pehle apne system me sirf ek library install karni padegi (baaki sab Python me pehle se aati hain). Apne terminal me yeh command chalao:
```bash
pip install pyttsx3