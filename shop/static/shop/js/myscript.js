$(document).ready(function () {
    $(".quick-view").click(function (e) {
    //   console.log(this.value);
      e.preventDefault();
      
      $.ajax({url: "",
      type: "GET",
      data: {id : this.value},
      success: function(result){
        $('.modal').modal('show');

        $('h3.modal-title').text("Quick View");
        $('h3.cost').html("$ "+result.price);
        $('#modal-desc').text(result.short_description);
        $('#modal-img').attr("src",result.image);
        $('#modal-title').text(result.name);

          },
      error: function() {
          console.log("error");
          }
      });
    });
  });