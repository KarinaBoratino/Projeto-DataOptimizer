$(document).ready(function () {
    $('#loginForm').on('submit', function (event) {
        event.preventDefault(); // Evita o envio padrão do formulário

        $.ajax({
            type: 'POST',
            url: $(this).attr('action'), // URL do formulário
            data: $(this).serialize(), // Serializa os dados do formulário
            success: function (response) {
                Swal.fire({
                    title: 'Sucesso!',
                    text: response.message,
                    icon: 'success',
                    confirmButtonText: 'OK'
                }).then(() => {
                    window.location.href = '/'; // Redirecionar após o login bem-sucedido
                });
            },
            error: function (xhr) {
                let errorMessage;
                try {
                    const response = JSON.parse(xhr.responseText);
                    errorMessage = response.message || "Ocorreu um erro inesperado.";
                } catch (e) {
                    errorMessage = "Ocorreu um erro inesperado.";
                }

                Swal.fire({
                    title: 'Erro!',
                    text: errorMessage,
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
            }
        });
    });
});