$(document).ready(function () {
    function clean_form_cep() {
        // Limpa valores do formulário de cep.
        $("#id_street").val("");
        $("#id_neighborhood").val("");
        $("#id_city").val("");
        $("#id_state").val("");
        $("#id_ibge").val("");
    }

    //Quando o campo cep perde o foco.
    $("#id_cep").blur(function () {

        //Nova variável "cep" somente com dígitos.
        var cep = $(this).val().replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep) {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if (validacep.test(cep)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                $("#id_street").val("...");
                $("#id_neighborhood").val("...");
                $("#id_city").val("...");
                $("#id_state").val("...");
                $("#id_ibge").val("...");

                //Consulta o webservice viacep.com.br/
                $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function (data) {

                    if (!("erro" in data)) {
                        //Atualiza os campos com os valores da consulta.
                        $("#id_street").val(data.logradouro);
                        $("#id_neighborhood").val(data.bairro);
                        $("#id_city").val(data.localidade);
                        $("#id_state").val(data.uf);
                        $("#id_ibge").val(data.ibge);
                    } //end if.
                    else {
                        //CEP pesquisado não foi encontrado.
                        clean_form_cep();
                        alert("CEP não encontrado.");
                    }
                });
            } //end if.
            else {
                //cep é inválido.
                clean_form_cep();
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            clean_form_cep();
        }
    });
});