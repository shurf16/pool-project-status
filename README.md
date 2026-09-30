# 🏊 Reed's Pool Status
 
A lightweight Flask website for the Reed's School swimming pool, built to replace manual texting for pool updates.
 
> 🚧 **Status: in progress.** This project is actively being built. See the [roadmap](#-roadmap) for what's done and what's next.
 
## 💡 Why I'm building this
 
As a lifeguard at Reed's School, I noticed two problems. Pool updates were being shared by manually texting people, and members would often arrive to find every lane already taken, then understandably complain. This website lets members **check how busy the pool is before they set off**, so they can choose a quieter time. Lifeguards can update the status in seconds from poolside.
 
## ✨ Features
 
**For members and staff**
- View the current **member and staff swim times**
- See **live pool busyness** at a glance (e.g. 🟢 Quiet · 🟠 Busy · 🔴 All lanes full / Closed), so members can decide whether to come now or later
**For lifeguards**
- Update the busyness status through a **PIN-protected lifeguard panel**
## 🔐 Security
 
Because the lifeguard panel changes what everyone sees, it needs protecting. Planned security measures:
 
- [ ] **Hashed PIN**: the PIN is stored as a hash (never in plain text) and checked with Werkzeug's `check_password_hash`
- [ ] **Brute-force protection**: limit PIN attempts and add a temporary lockout after repeated failures
- [ ] **CSRF protection**: forms protected with Flask-WTF so other sites can't submit updates on a user's behalf
- [ ] **Input validation**: only accept the allowed status values
- [ ] **Session timeout**: lifeguards are logged out automatically after inactivity
- [ ] **Secrets kept out of the code**: secret key and PIN hash loaded from environment variables, not committed to GitHub
- [ ] **Audit log**: record when the status was changed
## 🛠️ Built with
 
- **Python** + **Flask**: web app and routing
- **HTML / CSS**: pages and styling
- **JavaScript**: auto-refreshing the busyness status without reloading the page
## 🗺️ Roadmap
 
- [ ] Set up Flask project structure
- [ ] Home page showing swim times
- [ ] Busyness status display
- [ ] Lifeguard login with PIN
- [ ] Lifeguard panel to update the status
- [ ] Auto-refresh with JavaScript
- [ ] Add the security features above
- [ ] Mobile-friendly design
- [ ] Deploy online
## 🚀 Running it locally
 
*Instructions will be added once the first version is working.*
 
## 👤 Author
 
**Sophie Hurford**: Computer Science with Security student at Cardiff University
[GitHub](https://github.com/shurf16) · [LinkedIn](https://www.linkedin.com/in/sophie-hurford/)
 
