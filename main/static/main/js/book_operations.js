function add_book() {
  const csrftoken = document.cookie.toString().split("=")[1];
  var book_name = $("#book-name").val();
  var isbn = $("#isbn").val();
  if(book_name.trim()=="" || isbn.trim ==""){
      alert("Field cannot be empty");
      return;
  }
  $.ajax({
    url: "/book_api/",
    headers: {
      "X-CSRFToken": csrftoken,
    },
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      'name': book_name,
      'ISBN': isbn,
    }),
    success: function (data) {
      console.log(data);
        window.location.reload();
    },
    error: function (data) {
      console.log(data);
    },
  });
}

function update_book() {
  const csrftoken = document.cookie.toString().split("=")[1];
  var book_id = $("#book-id").text();
  var book_name = $("#book-name").val();
    var isbn = $("#isbn").val();
      if (book_name.trim() == "" || isbn.trim == "") {
        alert("Field cannot be empty");
        return;
      }
    $.ajax({
      url: "/book_api/" + book_id + "/",
      headers: {
        "X-CSRFToken": csrftoken,
      },
      type: "PUT",
      contentType: "application/json",
      data: JSON.stringify({
        'id': book_id,
        'name': book_name,
        'ISBN': isbn,
      }),
      success: function (data) {
        console.log(data);
        window.location.reload();
      },
      error: function (data) {
        console.log(data);
      },
    });
}

function delete_book() {
  const csrftoken = document.cookie.toString().split("=")[1];
  var book_id = $("#book-id").text();
  $.ajax({
    url: "/book_api/" + book_id,
    headers: {
      "X-CSRFToken": csrftoken,
    },
    type: "DELETE",
    data: JSON.stringify({
      id: book_id,
    }),
    success: function (data) {
      console.log(data);
      window.location.href = "/";
    },
    error: function (data) {
      console.log(data);
    },
  });
}

function get_book(book_id) {
  const csrftoken = document.cookie.toString().split("=")[1];
  $.ajax({
    url: "/book_api/" + book_id,
    headers: {
      "X-CSRFToken": csrftoken,
    },
    type: "GET",
    data: JSON.stringify({
      'id': book_id,
    }),
    success: function (data) {
      console.log(data["book"]);
      var book_name_field = $("#book-name");
      var isbn_field = $("#isbn");
      book_name_field.val(data["book"]["name"]);
      isbn_field.val(data["book"]["ISBN"]);
      $("#book-id").text(data["book"]["id"]);
    },
    error: function (data) {
      console.log(data);
    },
  });
}
