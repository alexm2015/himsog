NUM_CONTENTS = 4;
LAST_ID_NONE = 0;
category_slug = ''; 

g_last_id = 0;
/*TODO
    category_slug  
*/

// $(document).ready(function(){     
//    $(window).bind('scroll', loadOnScroll);
// });

$(document).ready(function(){
    console.log("GETTING DATA");
    loadItems(NUM_CONTENTS, LAST_ID_NONE, category_slug);
});

// Scroll globals
var lastID = -1; // The latest page loaded
var hasNextPage = true; // Indicates whether to expect another page after this one

// loadOnScroll handler
var loadOnScroll = function() {
   // If the current scroll position is past out cutoff point...
    if ($(window).scrollTop() > $(document).height() - ($(window).height()*2)) {
        // temporarily unhook the scroll event watcher so we don't call a bunch of times in a row
        $(window).unbind(); 
        // execute the load function below that will visit the JSON feed and stuff data into the HTML
        loadItems(NUM_CONTENTS, g_last_id, category_slug);
    }
};

var loadItems = function(num_items, last_id, cat_slug) {
    // If the next page doesn't exist, just quit now 
    if (hasNextPage === false) {
        return false
    }

    //selected_cat = $("#category-dropdown-menu").val();
    selected_cat = 'food-and-supplements'
    console.log('SELECTED CATEGORY: '+ selected_cat);
    // Update the page number
    //lastID = lastID + 1;
    // Configure the url we're about to hit
    
    $.ajax({
        url: '/himsog/get_contents/',
        data: {'last_id':last_id, 'cat_slug':cat_slug, 'num_items': num_items},
        dataType: 'json',
        success: function(response) {
            // Update global next page variable
            
            //json = JSON.parse(response['contents'])
            hasNextPage = true;//.hasNext;
            // Loop through all items

            contents = response['contents'];
            n = contents.length;
            if (n > 0){
                for (var i=0; i < n; i++) {
                    entry = document.createElement('li');

                    content_node =  "------<br/>"
                                    + "ID: " + contents[i].id + '<br/>'
                                    + "Title: " + contents[i].title + '<br/>'
                                    + "Rating: " + contents[i].rating + '<br/>'
                                    + "Views: " + contents[i].views + '<br/>'
                                    + "Desc: " + contents[i].description + '<br/>'
                                    + "------<br/>";

                    entry.appendChild(document.createTextNode(content_node));
                    $("#demo").append(content_node);// Do something with your json object response
                }
                g_last_id = contents[n-1].id;
            }
        },
        error: function(data) {
            // When I get a 400 back, fail safely
            $(window).bind('scroll', loadOnScroll);
        },
        complete: function(data, textStatus){
            // Turn the scroll monitor back on
            $(window).bind('scroll', loadOnScroll);
        }
    });
};