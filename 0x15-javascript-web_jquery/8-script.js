$(document).ready(function() {
    const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    $.get(apiUrl, (data) => {
        const movies = data.results;
        movies.forEach(movie => {
            $('UL#list_movies').append('<li>'+movie.title+'</li>');
        });
    });
});