# all_scripts.py

# Import your scripts
import appbanner
import desktop
import popup
import ppt
import push
import social

# Wrap each in a function that takes the input args
def run_appbanner(title, subtitle, logo, facimg1, facimg2,
                  facname1, facname2, facdesc1, facdesc2, date, time, reg):
    return appbanner.generate(title, subtitle, logo, facimg1, facimg2,
                              facname1, facname2, facdesc1, facdesc2, date, time, reg)

def run_desktop(title, subtitle, logo, facimg1, facimg2,
                facname1, facname2, facdesc1, facdesc2, date, time, reg):
    return desktop.generate(title, subtitle, logo, facimg1, facimg2,
                            facname1, facname2, facdesc1, facdesc2, date, time, reg)

def run_popup(title, subtitle, logo, facimg1, facimg2,
              facname1, facname2, facdesc1, facdesc2, date, time, reg):
    return popup.generate(title, subtitle, logo, facimg1, facimg2,
                          facname1, facname2, facdesc1, facdesc2, date, time, reg)

def run_ppt(title, subtitle, logo, facimg1, facimg2,
            facname1, facname2, facdesc1, facdesc2, date, time, reg):
    return ppt.generate(title, subtitle, logo, facimg1, facimg2,
                        facname1, facname2, facdesc1, facdesc2, date, time, reg)

def run_push(title, subtitle, logo, facimg1, facimg2,
             facname1, facname2, facdesc1, facdesc2, date, time, reg):
    return push.generate(title, subtitle, logo, facimg1, facimg2,
                         facname1, facname2, facdesc1, facdesc2, date, time, reg)

def run_social(title, subtitle, logo, facimg1, facimg2,
               facname1, facname2, facdesc1, facdesc2, date, time, reg):
    return social.generate(title, subtitle, logo, facimg1, facimg2,
                           facname1, facname2, facdesc1, facdesc2, date, time, reg)
