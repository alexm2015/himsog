(function (window) {
	'use strict';

	function Model() {}

	Model.prototype.get_category_list = function (callback) {
		callback = callback || function () {};

		$.ajax({
			method: "GET",
			url: "/himsog/category/"
		}).done(function(data) {
			callback(data["category_list"]);
		});
	};

	// Export to window
	window.app = window.app || {};
	window.app.CategoryModel = Model;
})(window);
