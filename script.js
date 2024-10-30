document.getElementById('reservaForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let isValid = true;

    const nome = document.getElementById('nome');
    const telefone = document.getElementById('telefone');
    const data = document.getElementById('data');
    const hora = document.getElementById('hora');
    const pessoas = document.getElementById('pessoas');

    // Limpar mensagens de erro
    document.querySelectorAll('.error').forEach(function(error) {
        error.style.display = 'none';
    });

    // Validações básicas
    if (!nome.value.trim()) {
        document.getElementById('error-nome').style.display = 'block';
        isValid = false;
    }

    if (!telefone.value.trim()) {
        document.getElementById('error-telefone').style.display = 'block';
        isValid = false;
    }

    if (!data.value) {
        document.getElementById('error-data').style.display = 'block';
        isValid = false;
    }

    if (!hora.value) {
        document.getElementById('error-hora').style.display = 'block';
        isValid = false;
    }

    if (!pessoas.value || pessoas.value <= 0) {
        document.getElementById('error-pessoas').style.display = 'block';
        isValid = false;
    }

    if (isValid) {
        alert('Reserva enviada com sucesso!');
        this.reset();
    }
});

document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const nomeReserva = document.getElementById("nomeReserva").value;
    const senha = document.getElementById("senha").value;
    alert(`Nome da Reserva: ${nomeReserva}\nSenha: ${senha}`);
});