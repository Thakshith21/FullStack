import subprocess

batch = "tesrty Mission JAIIb"
title = "5-Month Success Roadmap for Batch 3025"
examcode = "irdai"
engcode = "payal"
rescode = "himanshu"
engname = "Payal Maam"
resname = "Himanshu sir"
engdesig = "English Faculty"
resdesig = "Reasoning Faculty"
date = "June 8"
time = "11 PM"
cta = "Register Now"


subprocess.run([
    "python3", "appbanner.py",
    batch, title, examcode,
    engcode, rescode,
    engname, resname,
    engdesig, resdesig,
    date, time, cta
])

