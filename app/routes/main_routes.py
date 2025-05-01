from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def homepage():
    return render_template('homepage.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/references')
def references():
    return render_template('references.html')

# Product routes
@main.route('/flex-yazi-neon-tabelalar')
def flex_yazi_neon_tabelalar():
    return render_template('flex-yazi-neon-tabelalar.html')

@main.route('/flex-ozel-tasarim-neon-tabelalar')
def flex_ozel_tasarim_neon_tabelalar():
    return render_template('flex-ozel-tasarim-neon-tabelalar.html')

@main.route('/ic-mekan-led-tabelalar')
def ic_mekan_led_tabelalar():
    return render_template('ic-mekan-led-tabelalar.html')

@main.route('/dis-mekan-led-tabelalar')
def dis_mekan_led_tabelalar():
    return render_template('dis-mekan-led-tabelalar.html')

@main.route('/rgb-led-tabelalar')
def rgb_led_tabelalar():
    return render_template('rgb-led-tabelalar.html')

@main.route('/kayan-yazi-led-tabelalar')
def kayan_yazi_led_tabelalar():
    return render_template('kayan-yazi-led-tabelalar.html')

@main.route('/ic-mekan-led-ekranlar')
def ic_mekan_led_ekranlar():
    return render_template('ic-mekan-led-ekranlar.html')

@main.route('/dis-mekan-led-ekranlar')
def dis_mekan_led_ekranlar():
    return render_template('dis-mekan-led-ekranlar.html')

