# 🕒 Cron Job Locations – Quick Reference

## 📂 System-Wide Cron
- `/etc/cron.d/` → Drop custom cron files here (e.g., `/etc/cron.d/dashboard`).
- `/etc/crontab` → Main system crontab file (runs system tasks).
- `/etc/cron.daily/` → Scripts run once per day.
- `/etc/cron.hourly/` → Scripts run once per hour.
- `/etc/cron.weekly/` → Scripts run once per week.
- `/etc/cron.monthly/` → Scripts run once per month.

> ℹ️ **Note:** In `/etc/cron.d/` files, you must explicitly specify the user (e.g., `root`).

---

## 👤 User Cron
- Managed via `crontab -e`
- Stored at: `/var/spool/cron/crontabs/<username>`
- Runs as the given user.

---

## ✅ Example
System-wide cron job for the dashboard:

```cron
# /etc/cron.d/dashboard
@reboot root /opt/cyber-dash/scripts/start-dashboard.sh
0 3 * * * root /opt/cyber-dash/scripts/start-dashboard.sh
