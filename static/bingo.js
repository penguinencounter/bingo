function init_new_word () {
    let req = new XMLHttpRequest();
    req.open('GET', '/word/')
    req.addEventListener('load', new_word_ready);
    req.send();
}


function new_word_ready () {
    console.log(this.responseText);
}