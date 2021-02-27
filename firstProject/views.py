from django.shortcuts import render


def home(request):

    return render(request, 'PortfolioBoot.html')



def contact(request):

    return render(request, 'contactform.html')


def submission(request):
    user_name = request.GET['First Name']
    Email_Id = request.GET['Email_Id']
    Subject  = request.GET['Subject']
    Message = request.GET['Message']


    return render(request, 'Submission.html', {'submission_name': user_name, 'mail': Email_Id, 'submission_subject':Subject, 'submission_message': Message })
