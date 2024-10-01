  $(document).ready(function() {
            $('#cadastroForm').on('submit', function(event) {
                event.preventDefault();

                $.ajax({
                    type: 'POST',
                    url: $(this).attr('action'),
                    data: $(this).serialize(),
                    success: function(response) {
                        Swal.fire({
                            title: 'Sucesso!',
                            text: 'Usuário cadastrado com sucesso!',
                            icon: 'success',
                            confirmButtonText: 'OK'
                        }).then(() => {
                            window.location.href = '/';
                        });
                    },
                    error: function(xhr) {
                        // Tenta analisar a resposta JSON
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