$(document).ready(function () {

    var $window = $(window),
        // $banner = $('#banner'),
        $body = $('body');

    $window.on('load', function () {
        window.setTimeout(function () {
            $body.removeClass('is-preload');
        }, 100);
    });


    var form = $('#form_buying_product');

    function basketUpdating(product_id, count, is_delete) {
        var data_struct = {};
        data_struct.product_id = product_id;
        data_struct.product_count = count;
        data_struct["csrfmiddlewaretoken"] = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();

        if (is_delete) {
            data_struct["is_delete"] = true;
        }

        var url = form.attr('action');
        $.ajax({
            url: url,
            type: 'POST',
            data: data_struct,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data);
                console.log(data.products_total_number);
                if (data.products_total_number || data.products_total_number === 0) {
                    $('#basket_total_count').text("(" + data.products_total_number + ")");
                    $('.basket-items ul').html("");
                    $.each(data.products, function (k, v) {
                        $('.basket-items ul').append('<li>' + v.name + ', count: ' + v.count + '; ' +
                            'total cost: ' + v.product_total_price + '     ' +
                            '<a class="delete-item" style="color: white" href="" data-product_id="' + v.id + '">x</a>' +
                            '</li>');
                    })
                }
            },
            error: function () {
                console.log("ERROR");
            }
        })

    }

    form.on('submit', function (e) {
        e.preventDefault();

        var count = Number($('#number').val());
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');


        basketUpdating(product_id, count, is_delete = false);
    });

    function showingBasket() {
        $('.basket-items').fadeIn(1000);
    }

    $('#basket').mouseover(function () {
        showingBasket();
    });

    $('#close-basket').click(function () {
        $('.basket-items').fadeOut(1000);

    });


    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        var product_id = $(this).data("product_id");
        $(this).closest('li').remove();
        basketUpdating(product_id, 0, true);
    });

    // function calculateBasketAmount(product_id) {
    //     var total_order_amount = 0;
    //     $('.product-in-basket-total-price').each(function () {
    //         total_order_amount += parseInt($(this).text());
    //     });
    //     $('#total_order_amount').text(total_order_amount);
    //
    // }
});