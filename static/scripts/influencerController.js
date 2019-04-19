app.directive("matchPassword", function () {
    return {
        require: "ngModel",
        scope: {
            otherModelValue: "=matchPassword"
        },
        link: function(scope, element, attributes, ngModel) {

            ngModel.$validators.matchPassword = function(modelValue) {
                return modelValue == scope.otherModelValue;
            };

            scope.$watch("otherModelValue", function() {
                ngModel.$validate();
            });
        }
    };
});

//var images=[];

//$('document').ready(function(){
//
//    $('.image1').click(function(){
//        if($('.image1').hasClass('activeone')){
//            $('.image1').removeClass('activeone');
//        }// addClass('activeone');)
//        //$('.image').removeClass('activeone');
//        else
//        {
//            $(this).addClass('activeone');
//        }
//
//    });
//
//    $('.image2').click(function(){
//        if($('.image2').hasClass('activeone')){
//            $('.image2').removeClass('activeone');
//            $scope.areas.splice(index, 2);
//        }
//        else
//        {
//            $(this).addClass('activeone');
//            $scope.areas.push($('.image2'));
//        }
//    });
//
//    $('.image3').click(function(){
//        if($('.image3').hasClass('activeone')){
//            $('.image3').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image4').click(function(){
//        if($('.image4').hasClass('activeone')){
//            $('.image4').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image5').click(function(){
//        if($('.image5').hasClass('activeone')){
//            $('.image5').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image6').click(function(){
//        if($('.image6').hasClass('activeone')){
//            $('.image6').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image7').click(function(){
//        if($('.image7').hasClass('activeone')){
//            $('.image7').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//    $('.image8').click(function(){
//        if($('.image8').hasClass('activeone')){
//            $('.image8').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image9').click(function(){
//        if($('.image9').hasClass('activeone')){
//            $('.image9').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image10').click(function(){
//        if($('.image10').hasClass('activeone')){
//            $('.image10').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image11').click(function(){
//        if($('.image11').hasClass('activeone')){
//            $('.image11').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image12').click(function(){
//        if($('.image12').hasClass('activeone')){
//            $('.image12').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image13').click(function(){
//        if($('.image13').hasClass('activeone')){
//            $('.image13').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image14').click(function(){
//        if($('.image14').hasClass('activeone')){
//            $('.image14').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image15').click(function(){
//        if($('.image15').hasClass('activeone')){
//            $('.image15').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image16').click(function(){
//        if($('.image16').hasClass('activeone')){
//            $('.image16').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image17').click(function(){
//        if($('.image17').hasClass('activeone')){
//            $('.image17').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image18').click(function(){
//        if($('.image18').hasClass('activeone')){
//            $('.image18').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image19').click(function(){
//        if($('.image19').hasClass('activeone')){
//            $('.image19').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image20').click(function(){
//        if($('.image20').hasClass('activeone')){
//            $('.image20').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//    $('.image21').click(function(){
//        if($('.image21').hasClass('activeone')){
//            $('.image21').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image22').click(function(){
//        if($('.image22').hasClass('activeone')){
//            $('.image22').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image23').click(function(){
//        if($('.image23').hasClass('activeone')){
//            $('.image23').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image24').click(function(){
//        if($('.image24').hasClass('activeone')){
//            $('.image24').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image25').click(function(){
//        if($('.image25').hasClass('activeone')){
//            $('.image25').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image26').click(function(){
//        if($('.image26').hasClass('activeone')){
//            $('.image26').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image27').click(function(){
//        if($('.image27').hasClass('activeone')){
//            $('.image27').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//    $('.image28').click(function(){
//        if($('.image28').hasClass('activeone')){
//            $('.image28').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image29').click(function(){
//        if($('.image29').hasClass('activeone')){
//            $('.image29').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image30').click(function(){
//        if($('.image30').hasClass('activeone')){
//            $('.image30').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image31').click(function(){
//        if($('.image31').hasClass('activeone')){
//            $('.image31').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image32').click(function(){
//        if($('.image32').hasClass('activeone')){
//            $('.image32').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image33').click(function(){
//        if($('.image33').hasClass('activeone')){
//            $('.image33').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image34').click(function(){
//        if($('.image34').hasClass('activeone')){
//            $('.image34').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image35').click(function(){
//        if($('.image35').hasClass('activeone')){
//            $('.image35').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//    $('.image36').click(function(){
//        if($('.image36').hasClass('activeone')){
//            $('.image36').removeClass('activeone');
//        }
//        else
//        {
//            $(this).addClass('activeone');
//        }
//    });
//
//});
//

app.controller("influencerController", function ($scope, $window, $http, $location)
 {

 $scope.count=0;

 $scope.records1 = [
     {path:"/static/images/searchFilterImages/animals.jpg", index: 0, class: "", label:"animals"},
     {path:"/static/images/searchFilterImages/art.jpg", index: 1, class: "", label:"art"},
     {path:"/static/images/searchFilterImages/books.jpg", index: 2, class: "", label:"books"},
     {path:"/static/images/searchFilterImages/science.jpg", index: 3, class: "", label:"science"},
     ]
 $scope.records2 = [
      {path:"/static/images/searchFilterImages/tech.jpg", index: 0, class: "", label:"tech"},
      {path:"/static/images/searchFilterImages/business.jpg", index: 1, class: "", label:"business"},
      {path:"/static/images/searchFilterImages/causes.jpg", index: 2, class: "", label:"causes"},
      {path:"/static/images/searchFilterImages/comedy.jpg", index: 3, class: "", label:"comedy"},
      ]
 $scope.records3 = [
      {path:"/static/images/searchFilterImages/dance.jpg", index: 0, class: "", label:"dance"},
      {path:"/static/images/searchFilterImages/sport.jpg", index: 1, class: "", label:"sport"},
      {path:"/static/images/searchFilterImages/education.jpg", index: 2, class: "", label:"education"},
      {path:"/static/images/searchFilterImages/style.jpg", index: 3, class: "", label:"style"},
      ]
 $scope.records4 = [
      {path:"/static/images/searchFilterImages/entertainment.jpg", index: 0, class: "", label:"entertainment"},
      {path:"/static/images/searchFilterImages/beauty.jpg", index: 1, class: "", label:"beauty"},
      {path:"/static/images/searchFilterImages/photograph.jpg", index: 2, class: "", label:"photograph"},
      {path:"/static/images/searchFilterImages/family.jpg", index: 3, class: "", label:"family"},
      ]
 $scope.records5 = [
      {path:"/static/images/searchFilterImages/fashion.jpg", index: 0, class: "", label:"fashion"},
      {path:"/static/images/searchFilterImages/fitness.jpg", index: 1, class: "", label:"fitness"},
      {path:"/static/images/searchFilterImages/tv.jpg", index: 2, class: "", label:"tv"},
      {path:"/static/images/searchFilterImages/film.jpg", index: 3, class: "", label:"film"},
      ]
  $scope.records6 = [
       {path:"/static/images/searchFilterImages/DIY.jpg", index: 0, class: "", label:"DIY"},
       {path:"/static/images/searchFilterImages/gaming.jpg", index: 1, class: "", label:"gaming"},
       {path:"/static/images/searchFilterImages/food.jpg", index: 2, class: "", label:"food"},
       {path:"/static/images/searchFilterImages/lifestyle.jpg", index: 3, class: "", label:"lifestyle"},
       ]
  $scope.records7 = [
       {path:"/static/images/searchFilterImages/politics.jpg", index: 0, class: "", label:"politics"},
       {path:"/static/images/searchFilterImages/news.jpg", index: 1, class: "", label:"news"},
       {path:"/static/images/searchFilterImages/journalism.jpg", index: 2, class: "", label:"journalism"},
       {path:"/static/images/searchFilterImages/travel.jpg", index: 3, class: "", label:"travel"},
       ]
  $scope.records8 = [
       {path:"/static/images/searchFilterImages/radio.jpg", index: 0, class: "", label:"radio"},
       {path:"/static/images/searchFilterImages/music.jpg", index: 1, class: "", label:"music"}
       ]




 //$scope.class= false;


 $scope.addClass1 = function(val){
        if($scope.records1[val].class === "activeone" )
            $scope.records1[val].class = "";
        else
            $scope.records1[val].class = "activeone";
        //console.log('response',records[val].index);
      }
 $scope.addClass2 = function(val){
         if($scope.records2[val].class === "activeone" )
             $scope.records2[val].class = "";
         else
             $scope.records2[val].class = "activeone";
         //console.log('response',records[val].index);
       }
 $scope.addClass3 = function(val){
         if($scope.records3[val].class === "activeone" )
             $scope.records3[val].class = "";
         else
             $scope.records3[val].class = "activeone";
         //console.log('response',records[val].index);
       }
 $scope.addClass4 = function(val){
         if($scope.records4[val].class === "activeone" )
             $scope.records4[val].class = "";
         else
             $scope.records4[val].class = "activeone";
         //console.log('response',records[val].index);
       }
 $scope.addClass5 = function(val){
         if($scope.records5[val].class === "activeone" )
             $scope.records5[val].class = "";
         else
             $scope.records5[val].class = "activeone";
         //console.log('response',records[val].index);
       }
 $scope.addClass6 = function(val){
         if($scope.records6[val].class === "activeone" )
             $scope.records6[val].class = "";
         else
             $scope.records6[val].class = "activeone";
         //console.log('response',records[val].index);
       }
 $scope.addClass7 = function(val){
         if($scope.records7[val].class === "activeone" )
             $scope.records7[val].class = "";
         else
             $scope.records7[val].class = "activeone";
         //console.log('response',records[val].index);
       }
 $scope.addClass8 = function(val){
         if($scope.records8[val].class === "activeone" )
             $scope.records8[val].class = "";
         else
             $scope.records8[val].class = "activeone";
         //console.log('response',records[val].index);
       }

// $('.image1').click(function(){
//         if($('.image1').hasClass('activeone')){
//             $('.image1').removeClass('activeone');
//         }
//         else
//         {
//             $(this).addClass('activeone');
//         }
//
//     });


// for(x: records1){
//        if($('.image'+i).hasClass('activeone'))
//            $scope.areas.push('image'+i);
//    }

    //console.log($scope.cname)

    $scope.updateinflu = function() {

    $scope.areas=[];
    $scope.big_deal={"website":false, "insta":false, "youtube": false, "facebook": false, "other":false};

//        for(record: records1){
//             if(record.class === "activeone")
//                 $scope.areas.push(x.label);
//            }

        for (var i=0; i<4; i++) {
              if($scope.records1[i].class === "activeone")
                    $scope.areas.push($scope.records1[i].label);
            }
        for (var i=0; i<4; i++) {
              if($scope.records2[i].class === "activeone")
                    $scope.areas.push($scope.records2[i].label);
            }
        for (var i=0; i<4; i++) {
              if($scope.records3[i].class === "activeone")
                    $scope.areas.push($scope.records3[i].label);
            }
        for (var i=0; i<4; i++) {
              if($scope.records4[i].class === "activeone")
                    $scope.areas.push($scope.records4[i].label);
            }
        for (var i=0; i<4; i++) {
              if($scope.records5[i].class === "activeone")
                    $scope.areas.push($scope.records5[i].label);
            }
        for (var i=0; i<4; i++) {
              if($scope.records6[i].class === "activeone")
                    $scope.areas.push($scope.records6[i].label);
            }
        for (var i=0; i<4; i++) {
              if($scope.records7[i].class === "activeone")
                    $scope.areas.push($scope.records7[i].label);
            }
        for (var i=0; i<2; i++) {
              if($scope.records8[i].class === "activeone")
                    $scope.areas.push($scope.records8[i].label);
            }


        //if($('.image1').hasClass('activeone'))


        var data =
        {
            "first_name" : $scope.fname,
            "last_name" : $scope.lname,
            "email" : $scope.email,
            "password" : $scope.password,
            "confirm_password" : $scope.confirm_password,
            "big_deal_on_option1" : $scope.big_deal.website,
            "big_deal_on_option2" : $scope.big_deal.insta,
            "big_deal_on_option3" : $scope.big_deal.youtube,
            "big_deal_on_option4" : $scope.big_deal.facebook,
            "big_deal_on_option5" : $scope.big_deal.other,
            "website_social_media_handles" : $scope.socialmedia,
            "followers" : $scope.followers,
            "areas_of_interest": $scope.areas

        }

        $http.post('http://localhost:5000/influencer/signup', data).then(function (response) {

            if (response.data)

                $scope.msg = "Post Data Submitted Successfully!";

        }, function (response) {

            $scope.msg = "Service not Exists";

            $scope.statusval = response.status;

            $scope.statustext = response.statusText;

            $scope.headers = response.headers();

        });

    };

});