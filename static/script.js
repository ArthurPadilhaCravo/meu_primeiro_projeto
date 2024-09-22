document.addEventListener("DOMContentLoaded", function() {
    fetch('http://127.0.0.1:5000/api/mensagem')
        .then(response => response.json())
        .then(data => {
            document.getElementById('mensagem').innerText = data.mensagem;
        })
        .catch(error => {
            console.error('Erro ao consumir API:', error);
        });
});
