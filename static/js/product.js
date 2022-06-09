// product quantity button start for india //
$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
        // console.log(id)
    $.ajax({
        type: "GET",
        url: "/india/pluscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            document.getElementById("totalamoun").innerText = data.totalamount
            document.getElementById("shippingamount").innerText = data.shipping_amount
            document.getElementById("discount").innerText = data.discount
            document.getElementById("dis").innerText = data.dis
        }
    })
})

$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
        // console.log(id)
    $.ajax({
        type: "GET",
        url: "/india/minuscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            document.getElementById("totalamoun").innerText = data.totalamount
            document.getElementById("shippingamount").innerText = data.shipping_amount
            document.getElementById("discount").innerText = data.discount
            document.getElementById("dis").innerText = data.dis

        }
    })
})


// for remove botton for cart  start   //
$('.Remove-cart').click(function() {
        var id = $(this).attr("pid").toString();
        var eml = this
            // console.log(id)
        $.ajax({
            type: "GET",
            url: "/india/Removecart",
            data: {
                prod_id: id
            },
            success: function(data) {
                document.getElementById("amount").innerText = data.amount
                document.getElementById("totalamount").innerText = data.totalamount
                document.getElementById("totalamoun").innerText = data.totalamount
                document.getElementById("shippingamount").innerText = data.shipping_amount
                document.getElementById("discount").innerText = data.discount
                document.getElementById("dis").innerText = data.dis
                eml.parentNode.parentNode.parentNode.remove()
            }
        })
    })
    // product quantity button end for india //

// product quantity button start for usa //
$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
        // console.log(id)
    $.ajax({
        type: "GET",
        url: "/usa/pluscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity
            document.getElementById("amountusa").innerText = data.amountusa.toFixed(2);
            document.getElementById("totalamountusa").innerText = data.totalamountusa.toFixed(2);
            document.getElementById("totalamounusa").innerText = data.totalamountusa.toFixed(2);
            document.getElementById("Discountusa").innerText = data.discountusa.toFixed(2);
            document.getElementById("disusa").innerText = data.disusa.toFixed(2);
        }
    })
})

$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
        // console.log(id)
    $.ajax({
        type: "GET",
        url: "/usa/minuscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity
            document.getElementById("amountusa").innerText = data.amountusa.toFixed(2);
            document.getElementById("totalamountusa").innerText = data.totalamountusa.toFixed(2);
            document.getElementById("totalamounusa").innerText = data.totalamountusa.toFixed(2);
            document.getElementById("Discountusa").innerText = data.discountusa.toFixed(2);
            document.getElementById("disusa").innerText = data.disusa.toFixed(2);

        }
    })
})


// for remove botton for cart  start   //
$('.remove-cart').click(function() {
        var id = $(this).attr("pid").toString();
        var eml = this
            // console.log(id)
        $.ajax({
            type: "GET",
            url: "/usa/removecart",
            data: {
                prod_id: id
            },
            success: function(data) {
                document.getElementById("amountusa").innerText = data.amountusa
                document.getElementById("totalamountusa").innerText = data.totalamountusa
                document.getElementById("totalamounusa").innerText = data.totalamountusa
                document.getElementById("discountusa").innerText = data.discountusa
                document.getElementById("disusa").innerText = data.disusa
                eml.parentNode.parentNode.parentNode.remove()
            }
        })
    })
    // product quantity button end for usa //












$('.remove_add').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this
    console.log(id)
    $.ajax({
        type: "GET",
        url: "/india/removeadd",
        success: function() {
            eml.parentNode.parentNode.parentNode.remove()
        }
    })
})