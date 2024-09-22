// Função que faz uma requisição GET para a API
async function buscarMensagem() {
    try {
        // Faz a requisição para o endpoint da API
        const response = await fetch('http://127.0.0.1:5000/api/mensagem');
        
        // Verifica se a requisição foi bem-sucedida
        if (!response.ok) {
            throw new Error('Erro ao buscar mensagem da API');
        }
        
        // Converte a resposta em JSON
        const data = await response.json();
        
        // Exibe a mensagem retornada da API no console
        console.log(data.mensagem);

        // Exibe a mensagem na página HTML
        document.getElementById('mensagem').innerText = data.mensagem;
    } catch (error) {
        console.error('Erro:', error);
    }
}
