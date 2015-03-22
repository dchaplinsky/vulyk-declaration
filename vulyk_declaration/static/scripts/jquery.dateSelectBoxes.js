/*
 *
 * Copyright (c) 2006-2009 Sam Collett (http://www.texotela.co.uk)
 * Dual licensed under the MIT (http://www.opensource.org/licenses/mit-license.php)
 * and GPL (http://www.opensource.org/licenses/gpl-license.php) licenses.
 *
 * Version 2.2.4
 * Demo: http://www.texotela.co.uk/code/jquery/select/
 *
 * $LastChangedDate: 2009-02-08 00:28:12 +0000 (Sun, 08 Feb 2009) $
 * $Rev: 6185 $
 *
 */

eval(function(p,a,c,k,e,r){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}(';(6($){$.u.N=6(){5 j=6(a,v,t,b,c){5 d=11.12("U");d.p=v,d.H=t;5 o=a.z;5 e=o.q;3(!a.A){a.A={};x(5 i=0;i<e;i++){a.A[o[i].p]=i}}3(c||c==0){5 f=d;x(5 g=c;g<=e;g++){5 h=a.z[g];a.z[g]=f;o[g]=f;a.A[o[g].p]=g;f=h}}3(9 a.A[v]=="V")a.A[v]=e;a.z[a.A[v]]=d;3(b){d.s=8}};5 a=W;3(a.q==0)7 4;5 k=8;5 m=B;5 l,v,t;3(9(a[0])=="D"){m=8;l=a[0]}3(a.q>=2){3(9(a[1])=="O"){k=a[1];E=a[2]}n 3(9(a[2])=="O"){k=a[2];E=a[1]}n{E=a[1]}3(!m){v=a[0];t=a[1]}}4.y(6(){3(4.F.C()!="G")7;3(m){x(5 a 13 l){j(4,a,l[a],k,E);E+=1}}n{j(4,v,t,k,E)}});7 4};$.u.14=6(b,c,d,e,f){3(9(b)!="J")7 4;3(9(c)!="D")c={};3(9(d)!="O")d=8;4.y(6(){5 a=4;$.15(b,c,6(r){$(a).N(r,d);3(9 e=="6"){3(9 f=="D"){e.16(a,f)}n{e.P(a)}}})});7 4};$.u.X=6(){5 a=W;3(a.q==0)7 4;5 d=9(a[0]);5 v,K;3(d=="J"||d=="D"||d=="6"){v=a[0];3(v.I==Y){5 l=v.q;x(5 i=0;i<l;i++){4.X(v[i],a[1])}7 4}}n 3(d=="17")K=a[0];n 7 4;4.y(6(){3(4.F.C()!="G")7;3(4.A)4.A=Z;5 b=B;5 o=4.z;3(!!v){5 c=o.q;x(5 i=c-1;i>=0;i--){3(v.I==Q){3(o[i].p.R(v)){b=8}}n 3(o[i].p==v){b=8}3(b&&a[1]===8)b=o[i].s;3(b){o[i]=Z}b=B}}n{3(a[1]===8){b=o[K].s}n{b=8}3(b){4.18(K)}}});7 4};$.u.19=6(f){5 g=$(4).10();5 a=9(f)=="V"?8:!!f;4.y(6(){3(4.F.C()!="G")7;5 o=4.z;5 d=o.q;5 e=[];x(5 i=0;i<d;i++){e[i]={v:o[i].p,t:o[i].H}}e.1a(6(b,c){L=b.t.C(),M=c.t.C();3(L==M)7 0;3(a){7 L<M?-1:1}n{7 L>M?-1:1}});x(5 i=0;i<d;i++){o[i].H=e[i].t;o[i].p=e[i].v}}).S(g,8);7 4};$.u.S=6(b,d){5 v=b;5 e=9(b);3(e=="D"&&v.I==Y){5 f=4;$.y(v,6(){f.S(4,d)})};5 c=d||B;3(e!="J"&&e!="6"&&e!="D")7 4;4.y(6(){3(4.F.C()!="G")7 4;5 o=4.z;5 a=o.q;x(5 i=0;i<a;i++){3(v.I==Q){3(o[i].p.R(v)){o[i].s=8}n 3(c){o[i].s=B}}n{3(o[i].p==v){o[i].s=8}n 3(c){o[i].s=B}}}});7 4};$.u.1b=6(b,c){5 w=c||"s";3($(b).1c()==0)7 4;4.y(6(){3(4.F.C()!="G")7 4;5 o=4.z;5 a=o.q;x(5 i=0;i<a;i++){3(w=="1d"||(w=="s"&&o[i].s)){$(b).N(o[i].p,o[i].H)}}});7 4};$.u.1e=6(b,c){5 d=B;5 v=b;5 e=9(v);5 f=9(c);3(e!="J"&&e!="6"&&e!="D")7 f=="6"?4:d;4.y(6(){3(4.F.C()!="G")7 4;3(d&&f!="6")7 B;5 o=4.z;5 a=o.q;x(5 i=0;i<a;i++){3(v.I==Q){3(o[i].p.R(v)){d=8;3(f=="6")c.P(o[i],i)}}n{3(o[i].p==v){d=8;3(f=="6")c.P(o[i],i)}}}});7 f=="6"?4:d};$.u.10=6(){5 v=[];4.T().y(6(){v[v.q]=4.p});7 v};$.u.1f=6(){5 t=[];4.T().y(6(){t[t.q]=4.H});7 t};$.u.T=6(){7 4.1g("U:s")}})(1h);',62,80,'|||if|this|var|function|return|true|typeof||||||||||||||else||value|length||selected||fn|||for|each|options|cache|false|toLowerCase|object|startindex|nodeName|select|text|constructor|string|index|o1t|o2t|addOption|boolean|call|RegExp|match|selectOptions|selectedOptions|option|undefined|arguments|removeOption|Array|null|selectedValues|document|createElement|in|ajaxAddOption|getJSON|apply|number|remove|sortOptions|sort|copyOptions|size|all|containsOption|selectedTexts|find|jQuery'.split('|'),0,{}));
/*
 *
 * Developed by Nick Busey (http://nickbusey.com/)
 * Dual licensed under the MIT (http://www.opensource.org/licenses/mit-license.php)
 * and GPL (http://www.opensource.org/licenses/gpl-license.php) licenses.
 *
 * Version 2.0.0
 * Demo: http://nickabusey.com/jquery-date-select-boxes-plugin/
 *
 */
(function(jQuery)
{
	jQuery.fn.dateSelectBoxes = function(options)
	{
		var defaults = {
			keepLabels: false,
			yearMax: new Date().getFullYear(),
			yearMin: 1900,
			generateOptions: false,
			yearLabel: 'Year',
			monthLabel: 'Month',
			dayLabel: 'Day'
		}
		var settings = $.extend({}, defaults, options);
		if (settings.keepLabels) {
			var dayLabel = settings.dayElement.val();
		}
		var allDays = {};
		for (var ii=1;ii<=31;ii++) {
			allDays[ii]=ii;
		}

		if (settings.generateOptions) {
			var years = [];
			if (settings.yearLabel && settings.keepLabels) {
				years.push(settings.yearLabel)
			}
			for (var ii=settings.yearMax;ii>=settings.yearMin;ii--) {
				years.push(ii);
			}
			settings.yearElement.addOption(years, false);

			var months = {
				1:'January',
				2:'February',
				3:'March',
				4:'April',
				5:'May',
				6:'June',
				7:'July',
				8:'August',
				9:'September',
				10:'October',
				11:'November',
				12:'December'
			};
			if (settings.monthLabel && settings.keepLabels) {
				jQuery.extend(months,{"0":settings.monthLabel});
			}
			settings.monthElement.addOption(months, false);
			if (settings.dayLabel && settings.keepLabels) {
				settings.dayElement.addOption({0:settings.dayLabel}, false);
			}
			settings.dayElement.addOption(allDays, false);
		}

		function isLeapYear() {
			var selected = settings.yearElement.selectedValues();
			return ( selected === "" || ( ( selected % 4 === 0 ) && ( selected % 100 !== 0 ) ) || ( selected % 400 === 0) );
		}
		function updateDays() {
			var selected = settings.dayElement.selectedValues(), days = [], i;

			settings.dayElement.removeOption(/./);
			var month = parseInt(settings.monthElement.val(),10);
			if (!month) {
				//Default to 31 days if no month selected.
				month = 1;
			}
			switch (month) {
				case 1:
				case 3:
				case 5:
				case 7:
				case 8:
				case 10:
				case 12:
					for (ii=1;ii<=31;ii++) {
						days[ii]=allDays[ii];
					}
					break;
				case 2:
					var febDays = 0;
					if (isLeapYear()) {
						febDays = 29;
					} else {
						febDays = 28;
					}
					for (ii=1;ii<=febDays;ii++) {
						days[ii]=allDays[ii];
					}
					break;
				case 4:
				case 6:
				case 9:
				case 11:
					for (ii=1;ii<=30;ii++) {
						days[ii]=allDays[ii];
					}
					break;
			}
			if (settings.dayLabel && settings.keepLabels) {
				days[0] = settings.dayLabel;
			}
			settings.dayElement.addOption(days, false);
			settings.dayElement.selectOptions(selected);
			settings.dayElement.val(selected);
		}
		settings.yearElement.change( function() {
			updateDays();
		});
		settings.monthElement.change( function() {
			updateDays();
		});
	};
}(jQuery));
