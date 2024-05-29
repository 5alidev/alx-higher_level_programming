$(document).ready(function() {
    $('INPUT#btn_translate').click(() => {
        const langCode = $('INPUT#language_code').val();
        const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;
        $.get(apiUrl, (data) => {
            $('DIV#hello').text(data.hello);
        });
    });
});