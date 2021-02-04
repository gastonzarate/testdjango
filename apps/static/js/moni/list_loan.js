$(document).ready(()=>{
    let url_loans = $("#list-loan-script").data("url-loans")
    let loan_template = document.querySelector("#row-loan");
    let page = 1
    let num_pages=1       
    
    let getLoans=()=>{
        let request = $.ajax({
			type: "GET",
            url: url_loans,
            data:{
                page:page
            }
        });
        request.done((response)=>{
            let loans = response["results"]
            let loan, copy_loan_template
            
            if(loans.length>0){
                $(".list-empty").addClass("sr-only")
                $(".list-filled").removeClass("sr-only")
                $("table tbody").html("")

                num_pages=Math.ceil(response["count"]/5)
                $(".page").html(page)
                $(".num_pages").html(num_pages)


                for(i in loans){
                    loan = loans[i]
                    loan_template.content.querySelector(".row-loan").id = loan["id"]
                    loan_template.content.querySelector(".first-name").textContent = loan["first_name"]
                    loan_template.content.querySelector(".last-name").textContent = loan["last_name"]
                    loan_template.content.querySelector(".dni").textContent = loan["dni"]
                    loan_template.content.querySelector(".gender").textContent = loan["gender_name"]
                    loan_template.content.querySelector(".email").textContent = loan["email"]
                    loan_template.content.querySelector(".email").href = "mailto:"+loan["email"]
                    loan_template.content.querySelector(".amount").textContent = loan["amount"]
                    loan_template.content.querySelector(".status").textContent = loan["status_name"][1]
                    
                    copy_loan_template = document.importNode(
                        loan_template.content,
                        true
                    );
                    $("table tbody").append(copy_loan_template);
                }
            }else{
                $(".list-empty").removeClass("sr-only")
                $(".list-filled").addClass("sr-only")
            }
        })
    }
    getLoans()

    $("#pag-articles-next").click(()=>{
        if(page<num_pages){
            page++
            getLoans()
        }
    })

    $("#pag-articles-back").click(()=>{
        if(page>1){
            page--
            getLoans()
        }
    })

    $(document).on("click",".btn-delete",function(){
        let id = $(this).parent().parent().attr('id');
        deleteLoan(id)
    })

    let deleteLoan=(id)=>{
        let request = $.ajax({
            headers: { "X-CSRFToken": CSRF_TOKEN },
            type: "DELETE",
            contentType: "application/json",
            url: url_loans+id+"/",
        });
        request.done((response)=>{
            getLoans()
            alert('Se borro correctamente')
        })
        request.fail((response)=>{
            alert('Ocurrio un error al borrar')
        })
    }

    $(document).on("click",".btn-update",function(){
        let id = $(this).parent().parent().attr('id');
        $("#loan_id").val(id)
        
        $("#first_name_id").val($("#"+id+" .first-name").html())
        $("#last_name_id").val($("#"+id+" .last-name").html())
        $("#dni_id").val($("#"+id+" .dni").html())
        $("#email_id").val($("#"+id+" .email").html())
        $("#amount_id").val($("#"+id+" .amount").html())

        $("#gender_id option:contains("+$("#"+id+" .gender").html()+")").attr('selected', 'selected')

    })

    $(".btn-update-loan").click(()=>{
        let id = $("#loan_id").val()
        let first_name = $("#first_name_id").val()
        let last_name=$("#last_name_id").val()
        let dni = $("#dni_id").val()
        let email = $("#email_id").val()
        let amount = $("#amount_id").val()
        let gender = $("#gender_id").val()

        let request = $.ajax({
            headers: { "X-CSRFToken": CSRF_TOKEN },
            type: "PUT",
            url: url_loans+id+"/",
            data:{
                'first_name':first_name,
                'last_name':last_name,
                'dni':dni,
                'email':email,
                'amount':amount,
                'gender':gender
            }
        })
        request.done((response)=>{
            $("body").removeClass("modal-open");
            $("#updateModal").modal("hide")

            alert("Se actualizo correctamente el préstamo.")
            $("#"+id+" .first-name").html(first_name)
            $("#"+id+" .last-name").html(last_name)
            $("#"+id+" .dni").html(dni)
            $("#"+id+" .email").html(email)
            $("#"+id+" .amount").html(amount)
            $("#"+id+" .gender").html($("#gender_id option:selected" ).text())

        })
        request.fail((response)=>{
            let text_error = ""
            let errors = response.responseJSON
            for(field in errors){
                text_error += errors[field] +". "
            }
            alert(text_error)
        })
    })
})