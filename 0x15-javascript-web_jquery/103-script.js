$(document).ready(function() {
    $('INPUT#btn_translate').click(() => {
        helloTranslate();
    });
    $('body').keypress((e) => {
        if (e.which === 13) {
            helloTranslate();
        }
    });
    const helloTranslate = () => {
        const langCode = $('INPUT#language_code').val();
        const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;
        $.get(apiUrl, (data) => {
            $('DIV#hello').text(data.hello);
        });
    }
});