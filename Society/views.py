from django.shortcuts import render
from django.http import JsonResponse
from .forms import SocietyRegistrationForm
import uuid
from .models import Society

# Create your views here.
def index(request):
    return render(request,'index.html')
from django.shortcuts import render
from django.http import JsonResponse
from .forms import SocietyRegistrationForm
from .models import Society
import uuid


def register_society(request):
    secretary_uid = None
    resident_uid = None
    
    if request.method == 'POST':
        form = SocietyRegistrationForm(request.POST)
        if form.is_valid():
            society = form.save(commit=False)
            secretary_uid = uuid.uuid4()
            resident_uid = uuid.uuid4()
            society.secretary_uid = secretary_uid
            society.resident_uid = resident_uid
            society.save()
            return render(request, 'register_society.html', {'form': form, 'secretary_uid': secretary_uid, 'resident_uid': resident_uid})
    else:
        form = SocietyRegistrationForm()
    return render(request, 'register_society.html', {'form': form, 'secretary_uid': secretary_uid, 'resident_uid': resident_uid})
# views.py

# views.py


# views.py

# views.py
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Society
from .forms import ResidentProblemForm
def submit_problem(request, society_uid):
    society = get_object_or_404(Society, resident_uid=society_uid)
    if request.method == 'POST':
        form = ResidentProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.society = society
            problem.save()
            return redirect('problem_submission_success')
    else:
        form = ResidentProblemForm()  # Make sure to initialize the form
    return render(request, 'submit_problem.html', {'form': form, 'society': society})


from django.shortcuts import render, redirect
from .forms import ResidentUIDForm
from .models import Society

# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Society

from django.shortcuts import render
from .models import Society
from django.urls import reverse
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse,HttpResponseBadRequest
from .models import Society

def enter_uid(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        try:
            society = Society.objects.get(resident_uid=uid)
            # Render the template with the society name
            return redirect(reverse('submit_problem', kwargs={'society_uid': uid}))
        except Society.DoesNotExist:
           
            return HttpResponseBadRequest('<h1>Invalid UUID</h1><p>The provided UUID is invalid.</p>')
    else:
        return render(request, 'enter_uid.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Society

def problem_submission_success(request):
    # Fetch the total pending problems count here
    pending_problems_count = ResidentProblem.objects.filter(solved=False).count()
    
    return render(request, 'problem_submission_success.html', {'pending_problems_count': pending_problems_count})
from django.shortcuts import render, get_object_or_404
from .models import Society

from django.shortcuts import render, redirect, get_object_or_404
from .models import Society


def secretary_problems(request, secretary_uid):
    # Retrieve the society based on the provided secretary_uid
    society = get_object_or_404(Society, secretary_uid=secretary_uid)

    # Fetch all problems associated with the society
    problems = society.resident_problems.all()

    # Render a template to display the problems
    return render(request, 'secretary_problems.html', {'problems': problems, 'society': society})

def secretary_uid_form(request):
    if request.method == 'POST':
        # Retrieve the secretary_uid entered by the secretary
        secretary_uid = request.POST.get('secretary_uid')
        # Redirect to the URL containing the secretary UID
        return redirect('secretary_problems', secretary_uid=secretary_uid)
    else:
        # If it's a GET request, render the form template
        return render(request, 'secretary_uid_form.html')
from django.http import JsonResponse
from .models import ResidentProblem

# views.py
from django.http import JsonResponse
from .models import ResidentProblem
# views.py
from django.http import JsonResponse
from .models import ResidentProblem
# views.py
from django.http import JsonResponse
from .models import ResidentProblem

def solve_problem(request):
    if request.method == 'POST' and request.POST.get('ajax') == 'true':
        problem_id = request.POST.get('problem_id')
        try:
            problem = ResidentProblem.objects.get(pk=problem_id)
            problem.delete()  # Delete the problem object
            return JsonResponse({'success': True})
        except ResidentProblem.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Problem not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})
def view_pending_requests(request):
    return render(request, 'pending_requests.html')
from django.shortcuts import render, redirect
from .models import ResidentProblem

def view_pending_problems(request):
    if request.method == 'POST':
        resident_uid = request.POST.get('resident_uid')
        return redirect('view_pending_problems_resident', resident_uid=resident_uid)
    return render(request, 'resident_uid_input.html')
from django.shortcuts import render, redirect
from .models import ResidentProblem

def view_pending_problems_resident(request, resident_uid):
    pending_problems = ResidentProblem.objects.filter(society__resident_uid=resident_uid, solved=False)
    return render(request, 'pending_problems.html', {'resident_uid': resident_uid, 'pending_problems': pending_problems})
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)


