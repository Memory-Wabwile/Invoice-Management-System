$(document).ready(function(){
    // alert("tupo site !!!");
    $('#div_id_line_five , #div_id_line_five_quantity , #div_id_line_five_unit_price , #div_id_line_five_total_price ,#div_id_line_six , #div_id_line_six_quantity , #div_id_line_six_unit_price , #div_id_line_six_total_price , #div_id_line_seven , #div_id_line_seven_quantity , #div_id_line_seven_unit_price , #div_id_line_seven_total_price , #div_id_line_eight , #div_id_line_eight_quantity , #div_id_line_eight_unit_price , #div_id_line_eight_total_price , #div_id_line_nine , #div_id_line_nine_quantity , #div_id_line_nine_unit_price , #div_id_line_nine_total_price , #div_id_line_ten , #div_id_line_ten_quantity , #div_id_line_ten_unit_price , #div_id_line_ten_total_price ').hide()

    $('#more-line').click(function(){
        $('#div_id_line_five , #div_id_line_five_quantity , #div_id_line_five_unit_price , #div_id_line_five_total_price').slideToggle(200)
        $('#div_id_line_six , #div_id_line_six_quantity , #div_id_line_six_unit_price , #div_id_line_six_total_price').slideToggle(200)
        $('#div_id_line_seven , #div_id_line_seven_quantity , #div_id_line_seven_unit_price , #div_id_line_seven_total_price').slideToggle(200)
        $('#div_id_line_eight , #div_id_line_eight_quantity , #div_id_line_eight_unit_price , #div_id_line_eight_total_price').slideToggle(200)
        $('#div_id_line_nine , #div_id_line_nine_quantity , #div_id_line_nine_unit_price , #div_id_line_nine_total_price').slideToggle(200)
        $('#div_id_line_ten , #div_id_line_ten_quantity , #div_id_line_ten_unit_price , #div_id_line_ten_total_price').slideToggle(200)
    });

    $('#id_line_one_quantity , #id_line_one_unit_price , #id_line_two_quantity , #id_line_two_unit_price , #id_line_three_quantity , #id_line_three_unit_price , #id_line_four_quantity , #id_line_four_unit_price , #id_line_five_quantity , #id_line_five_unit_price , #id_line_six_quantity , #id_line_six_unit_price ,  #id_line_seven_quantity , #id_line_seven_unit_price ,  #id_line_eight_quantity , #id_line_eight_unit_price , #id_line_nine_quantity , #id_line_nine_unit_price , #id_line_ten_quantity , #id_line_ten_unit_price ,  ')
    var line_one_quantity_text = $('#id_line_one_quantity').val();
    var line_one_unit_price_text = $('#id_line_one_unit_price').val();
    var line_one_total = line_one_quantity_text * line_one_unit_price_text
}); 