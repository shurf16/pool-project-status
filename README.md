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
 
Because the lifeguard panel changes what everyone sees, it needs protecting. This is a core focus of the project, and I'm using it as a chance to learn proper security practices.

Planned:
- [ ] **Input validation**: only accept the allowed status values
- [ ] **Limit PIN attempts**
- [ ] **Audit log**: record when the status was changed
Learning as I build: temporary lockouts after repeated failed attempts, hashed Pin storage, and session timeouts. These will be added (and documented properly) once I understand them, not before.

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
 
**Sophie Hurford**: Computer Science with Security and Forensics (Year in Industry) student at Cardiff University
[GitHub](https://github.com/shurf16) · [LinkedIn](https://www.linkedin.com/in/sophie-hurford/)
 
