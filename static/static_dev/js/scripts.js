$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        console.log('123');
        var count = Number($('#number').val());
        console.log(count);

        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('product_name');
        var product_price = submit_btn.data('product_price');


        // console.log(product_id);
        // console.log(product_name);

        var data = {};
        data.product_id = product_id;
        data.product_count = count;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr('action');

        // console.log(data);
        // $.ajax({
        //     url: url,
        //     type: 'POST',
        //     date: data,
        //     cache: true,
        //     success: function (data) {
        //         console.log("OK");
        //     },
        //     error: function () {
        //         console.log("ERROR")
        //
        //     }
        // });


        $('.basket-items ul').append('<li>' + product_name + ', ' + 'count:' + count + ', price: ' + product_price +
            ', total cost:' + product_price * count +
            '<a class="delete-item" href="">    x</a>' +
            '</li>'
        )
    });

    function showingBasket() {
        $('.basket-items').toggleClass('d-none');
    }

    $('#basket').on('click', function (e) {
        e.preventDefault();
        showingBasket();
    });


    // $('.basket-container').mouseover(function () {
    //     showingBasket();
    // });

    //
    // $('.basket-container').mouseout(function () {
    //     showingBasket();
    // });

    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        $(this).closest('li').remove();
    })


});