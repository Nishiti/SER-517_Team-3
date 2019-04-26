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

$('document').ready(function(){

    $('.image1').click(function(){
        if($('.image1').hasClass('activeone')){
            $('.image1').removeClass('activeone');
        }// addClass('activeone');)
        //$('.image').removeClass('activeone');
        else
        {
            $(this).addClass('activeone');
        }

    });

    $('.image2').click(function(){
        if($('.image2').hasClass('activeone')){
            $('.image2').removeClass('activeone');
            $scope.areas.splice(index, 2);
        }
        else
        {
            $(this).addClass('activeone');
            $scope.areas.push($('.image2'));
        }
    });

    $('.image3').click(function(){
        if($('.image3').hasClass('activeone')){
            $('.image3').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image4').click(function(){
        if($('.image4').hasClass('activeone')){
            $('.image4').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image5').click(function(){
        if($('.image5').hasClass('activeone')){
            $('.image5').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image6').click(function(){
        if($('.image6').hasClass('activeone')){
            $('.image6').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image7').click(function(){
        if($('.image7').hasClass('activeone')){
            $('.image7').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });
    $('.image8').click(function(){
        if($('.image8').hasClass('activeone')){
            $('.image8').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image9').click(function(){
        if($('.image9').hasClass('activeone')){
            $('.image9').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image10').click(function(){
        if($('.image10').hasClass('activeone')){
            $('.image10').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image11').click(function(){
        if($('.image11').hasClass('activeone')){
            $('.image11').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image12').click(function(){
        if($('.image12').hasClass('activeone')){
            $('.image12').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image13').click(function(){
        if($('.image13').hasClass('activeone')){
            $('.image13').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image14').click(function(){
        if($('.image14').hasClass('activeone')){
            $('.image14').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image15').click(function(){
        if($('.image15').hasClass('activeone')){
            $('.image15').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image16').click(function(){
        if($('.image16').hasClass('activeone')){
            $('.image16').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image17').click(function(){
        if($('.image17').hasClass('activeone')){
            $('.image17').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image18').click(function(){
        if($('.image18').hasClass('activeone')){
            $('.image18').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image19').click(function(){
        if($('.image19').hasClass('activeone')){
            $('.image19').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image20').click(function(){
        if($('.image20').hasClass('activeone')){
            $('.image20').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });
    $('.image21').click(function(){
        if($('.image21').hasClass('activeone')){
            $('.image21').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image22').click(function(){
        if($('.image22').hasClass('activeone')){
            $('.image22').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image23').click(function(){
        if($('.image23').hasClass('activeone')){
            $('.image23').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image24').click(function(){
        if($('.image24').hasClass('activeone')){
            $('.image24').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image25').click(function(){
        if($('.image25').hasClass('activeone')){
            $('.image25').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image26').click(function(){
        if($('.image26').hasClass('activeone')){
            $('.image26').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image27').click(function(){
        if($('.image27').hasClass('activeone')){
            $('.image27').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });
    $('.image28').click(function(){
        if($('.image28').hasClass('activeone')){
            $('.image28').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image29').click(function(){
        if($('.image29').hasClass('activeone')){
            $('.image29').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image30').click(function(){
        if($('.image30').hasClass('activeone')){
            $('.image30').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image31').click(function(){
        if($('.image31').hasClass('activeone')){
            $('.image31').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image32').click(function(){
        if($('.image32').hasClass('activeone')){
            $('.image32').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image33').click(function(){
        if($('.image33').hasClass('activeone')){
            $('.image33').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image34').click(function(){
        if($('.image34').hasClass('activeone')){
            $('.image34').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image35').click(function(){
        if($('.image35').hasClass('activeone')){
            $('.image35').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

    $('.image36').click(function(){
        if($('.image36').hasClass('activeone')){
            $('.image36').removeClass('activeone');
        }
        else
        {
            $(this).addClass('activeone');
        }
    });

});


var influencerController = app.controller("influencerController", function ($scope, $window) {
 {

 for(i=1; i<=30; i++){
        if($('.image'+i).hasClass('activeone'))
            $scope.areas.push('image'+i);
    }

    //console.log($scope.cname)

    $scope.updateinflu = function() {

        f

        if($('.image1').hasClass('activeone'))


        var data =
        {
            "first_name" : $scope.fname,
            "last_name" : $scope.lname,
            "email" : $scope.email,
            "password" : $scope.password,
            "confirm_password" : $scope.confirm_password,
            "big_deal_on_option1" : $scope.website,
            "big_deal_on_option2" : $scope.insta,
            "big_deal_on_option3" : $scope.youtube,
            "big_deal_on_option4" : $scope.facebook,
            "big_deal_on_option5" : $scope.other,
            "website_social_media_handles" : $scope.socialmedia,
            "followers" : $scope.followers,
            "areas": $scope.areas

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