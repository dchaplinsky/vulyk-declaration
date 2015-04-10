;
var scripts = scripts || {};

scripts.Common = {

	initializeCache: function() {

		var $cache = {};

		$cache.html = $('html');
		$cache.body = $('body');

		this.$cache = $cache;
	},

	detecting: function () {
		this.$cache.html.removeClass('no-js');
	},

	isModernBrowser: function () {
		if ( // modernizer alternative
		'querySelector' in document &&
		'localStorage' in window &&
		'addEventListener' in window
		) {
			return true;
		} else {
			return false;
		}
	},

	globalInit: function() {
		this.$cache.body.on('click', ".weiss-form__input-act input[type='checkbox']", function() {
			var self = $(this);

			self.parent().toggleClass('js-ico-checked');
			self.parents('.weiss-form__input-w-ico').toggleClass('weiss-form__input-act_' + self.data('input-type') );
		});
	},

	jsPlaceholderInit: function () {
		$('input[placeholder], textarea[placeholder]').placeholder();
	},

	toggleFormSection: function(enableOnValue) {
		var trueValue = (typeof enableOnValue === "undefined") ? "other" : enableOnValue,
			ctrlInput = $(".js-related-control").find("input[type='checkbox'], select");

		function enabled(el) {
			return (el.value == "other" || el.checked);
		}

		function toggleSection(el, checked) {
			var sectionBlc = el.parents(".js-related-control").next(".js-related-section");

			sectionBlc[checked ? "removeClass" : "addClass"]("i-inputs_disabled");
			sectionBlc.find("input, select, textarea").attr("disabled", !checked);
		}

		ctrlInput.each(function() {
			toggleSection($(this), enabled(this));
		});

		ctrlInput.on('change', function() {
			toggleSection($(this), enabled(this));
		});
	},

	inputActions: function() {
		var $inputs = $('input[data-inp-act], select[data-inp-act], textarea[data-inp-act]');

		$inputs.wrap("<span class='weiss-form__input-w-ico'></span>");
		$('<i class="weiss-form__input-w-ico__ico weiss-form__input-act"></i>').insertAfter($inputs);

		$inputs.each(function() {
			var $input = $(this),
				$inputName = $input.attr('name'),
				$inputActions = $input.data('inp-act').split(',');

			$.each($inputActions, function (key, value) {
				var title;

				switch (value) {
					case "hidden":
						var title = 'Поле містить приховану інформацію';
						break;
					case "unclear":
						var title = 'Поле містить нерозбірливу інформацію';
						break;
				}

				$($input.next('.weiss-form__input-w-ico__ico'))
					.append('<label class="i-weiss-ico i-weiss-ico_'+ value +'" role="button" title="'+ title +'">' +
					'<input type="checkbox" name="'+ $inputName.replace(/\]$/, "") + '_' + value +']" tabindex="-1" data-input-type="' + value +'" /></label>');
			});
		});
	},

	inputActionsReInit: function(container) {
		var input = container.find(".weiss-form__input-act input[type='checkbox']");

		input.each(function() {
			var self =$(this);

			if (self.checked) {
				self.parent().addClass('js-ico-checked');
				self.parents('.weiss-form__input-w-ico').addClass('weiss-form__input-act_' + self.data('input-type') );
			} else {
				self.parent().removeClass('js-ico-checked');
				self.parents('.weiss-form__input-w-ico').removeClass('weiss-form__input-act_' + self.data('input-type') );
			}
		});
	},

	cloneyaInit: function () {
		var $clonewrapper = $('.js-clone-wrapper');

		$clonewrapper.cloneya({
			limit: 2000,
			cloneThis: '.js-toclone',
			valueClone: false,
			dataClone: false,
			deepClone: false,
			cloneButton: '.js-clone',
			deleteButton: '.js-clone-delete',
			clonePosition: 'after',
			serializeID: false,
			ignore: '.weiss-form__msg, .js-clone-ignore, .ui-autocomplete',
			defaultRender: true,
			preserveChildCount: true
		});
	},

	addAutoComplete: function(elem, source) {
		var $elemPar = $(elem).parent();

		$(elem).autocomplete({
			source: function(request, response) {
				var results = $.ui.autocomplete.filter(source, request.term);

				response(results.slice(0, 7));
			},
			appendTo: $elemPar
		});
	},

	dateSelectBoxesInit: function () {
		$().dateSelectBoxes({
			monthElement: $('#declaration__date_month'),
			dayElement: $('#declaration__date_day'),
			yearElement: $('#declaration__date_year'),
			keepLabels: true,
			yearLabel: 'Рік',
			monthLabel: 'Місяць',
			dayLabel: 'День'
		});
	},

	jqueryValidateInit: function () {

		$.validator.addMethod("lettersonly", function(value, element) {
			return this.optional(element) || /^[а-яА-ЯёЁіІїЇєЄ’`'ґҐa-zA-Z]+$/i.test(value);
		}, "Tільки букви, будьласка");

		$.validator.addMethod("lastnameonly", function(value, element) {
			return this.optional(element) || /^[а-яА-ЯёЁіІїЇєЄ’`'ґҐa-zA-Z\-]+$/i.test(value);
		}, "Tільки букви, будьласка");

		$.validator.addMethod("fractdigitsonly", function(value, element) {
			return this.optional(element) || /^\d+([\.,]\d+)?$/i.test(value);
		}, "Вводити потрібно лише цифри");

		$.validator.addClassRules({
			'js-is-LettersOnly': {
				lettersonly: true
			},
			'js-is-DigitsOnly': {
				fractdigitsonly: true
			},
			'js-is-lastnameonly': {
				lastnameonly: true
			},
			'js-is-strictDigitsOnly': {
				digits: true
			}
		});

		var $form = $('#form-declaration'),
			validateSettings = {
				errorClass: "js-invalid",
				errorElement: "p",
				errorPlacement: function (error, element) {
					if (element.attr('required')) {
						error.insertBefore(element).addClass('weiss-form__msg weiss-form__msg_error');
					} else {
						error.insertBefore(element).addClass('weiss-form__msg weiss-form__msg_warn');
					}
				},
				focusInvalid: false,
				invalidHandler: function(form, validator) {
					if (!validator.numberOfInvalids())
						return;

					$('html, body').animate({
						scrollTop: $(validator.errorList[0].element).offset().top - 60
					}, 200);

				}
			},
			validateThis = $form.validate(validateSettings),
			current = 0,
			content = $('.js-tab-content');

		this.$cache.body.on('reset', $form, function () {
			$form.validate().resetForm();
		}).on('click', '#intro__isnotdeclaration', function () {
			if($(this).is(':checked')) {
				$form.validate().settings.ignore = "*"; // disable all validation
			} else {
				$form.validate().settings.ignore = "";
			}
		});

		content.hide();
		$(content[0]).show();

		this.$cache.body.on('click', '.js-section-go', function(e) {
			if (!$(this).is('[type="reset"]')) {
				e.preventDefault();
			}

			var self = $(this),
				section = self.data('section-go'),
				goTo = '#section-' + section,
				showSection = function () {
					current = section;
					content.hide();
					$(goTo).fadeIn(400);
					$('html, body').animate({scrollTop:0}, 500);
				};

			if (validateThis.form()) { // this validate only current section. If we skip some sections they dont validating.
				showSection();
			} else {
				return false;
			}
		});

	},

	init: function () {
		var scrpt = this;

		scrpt.initializeCache();
		scrpt.detecting();
		scrpt.globalInit();

		$(function () { // DOM Ready
			var template = Handlebars.compile($('#decl_form_template').html()),
				output = $("#form-wrapper");

			scrpt.$cache.body.on("vulyk.next", function(e, data) {
				scrpt.$cache.html.scrollTop(0);
				output.html(template(data.result.task.data));
				scrpt.jqueryValidateInit();
				scrpt.toggleFormSection();
				scrpt.inputActions();
				scrpt.cloneyaInit();
				scrpt.dateSelectBoxesInit();
				scrpt.addAutoComplete("#general__last-name", scripts.Data.autocompliteData.lastname);
				scrpt.addAutoComplete("#general__name", scripts.Data.autocompliteData.firstname);
				scrpt.addAutoComplete("#general__patronymic", scripts.Data.autocompliteData.patronymic);
				scrpt.addAutoComplete("#general__place_district", scripts.Data.autocompliteData.districts);
				scrpt.addAutoComplete("#general__post_office", scripts.Data.autocompliteData.offices);
				scrpt.addAutoComplete("#vehicle__35__brand", scripts.Data.autocompliteData.cars);
				scrpt.addAutoComplete("#vehicle__36__brand", scripts.Data.autocompliteData.trucks);
				scrpt.addAutoComplete("#vehicle__37__brand", scripts.Data.autocompliteData.boats);
				scrpt.addAutoComplete("#vehicle__39__brand", scripts.Data.autocompliteData.motos);
			}).on("vulyk.save", function(e, callback) {
				var $form = $('#form-declaration'),
					data = $form.serializeJSON();

				if ($("#section-4").is(":visible") || $("#intro__isnotdeclaration").is(":checked")) {
					$form.remove();
					callback(data);
				} else {
					scrpt.$cache.html.scrollTop(0);
				}
			}).on("vulyk.skip", function(e, callback) {
				$('#form-declaration').remove();
				callback();
			});
		});

		return scrpt;
	}
};

scripts.Common.init();
