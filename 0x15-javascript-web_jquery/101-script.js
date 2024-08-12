$('document').ready(function(){
$('DIV#add_item').click(function(){
 $('UL.my_list').append('<li>Add item</li>');
$('DIv#remove_item').click(function(){
 $('UL.my_list li:last').remove()
$('DIV#Clear_list').click(function(){
 $('UL.my_list').empty();
})
})
})
})
