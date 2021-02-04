$(document).ready(()=>{
//------------------LOANS---------------------------------------
    let url_loan = $("#new-loan-script").data("url-loan")

    let showForm = () =>{
        $(".loan-result").addClass("sr-only")
        $(".loan-aprroved").addClass("sr-only")
        $(".loan-rejected").addClass("sr-only")
        $(".loan-error").addClass("sr-only")
        $(".loan-form").removeClass("sr-only")
    }

    let setErrorForm = (error) =>{
        $(".error").html(error)
    }

    let applyLoan=()=>{
        let first_name = $("#first_name_id").val()
        let last_name = $("#last_name_id").val()
        let email = $("#email_id").val()
        let dni = $("#dni_id").val()
        let gender = $("#gender_id").val()
        let amount = $("#amount_id").val()

        let request = $.ajax({
			type: "POST",
            url: url_loan,
            data:{
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "dni": dni,
                "gender": gender,
                "amount": amount
            }
        });
        request.done((response)=>{
            $(".loan-waiting").addClass("sr-only")
            $(".email").html(response.email)
            if(response.status===2){
                $(".loan-aprroved").removeClass("sr-only")
            }else if (response.status==3){
                $(".loan-rejected").removeClass("sr-only")
            }else{
                $(".loan-error").removeClass("sr-only")
            }
            setErrorForm("")
        })
        request.fail((response)=>{
            let text_error = ""
            let errors = response.responseJSON
            for(field in errors){
                text_error += errors[field] +"<br>"
            }
            $(".loan-waiting").addClass("sr-only")
            showForm()
            setErrorForm(text_error) 
        })
    }


    $(".btn-new-loan").click(()=>{
        showForm()
    })

    $(".btn-loan").click((event)=>{
        event.preventDefault();
         // Si el form no es valido
        var form = document.getElementById('form');

        if (!form.checkValidity()) {
            return false;
        }
        $(".loan-form").addClass("sr-only")
        $(".loan-result").removeClass("sr-only")
        $(".loan-waiting").removeClass("sr-only")
        applyLoan()
    })
//------------------END LOANS---------------------------------------
})