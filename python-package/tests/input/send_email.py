import smtplib


def e(u, p, t, m):
    s = smtplib.SMTP("smtp.example.com", 587)
    s.starttls()
    s.login(u, p)
    s.sendmail(u, t, m)
    s.quit()
