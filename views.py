from django.shortcuts import render
from django.db import models
from django.http import request
from divyaChemicalsWeb.models import otherMaintananceProducts,aboutPage,blogPage,blogHero,civilProducts,electricalProducts,contactPage, clientelePage,homePage,agrochemicalsPortfolio, chemicalPortfolio,  engieeringAutomobilesPortfolio , fertilizerPortfolio, foodPharmaPortfolio, glassCeramicPortfolio,homeHeroImage,homeProducts,mechanicalProducts, metalPortfolio, oilGasPortfolio, powerWindPortfolio,services,servicesPage,strength, team,testimonial,tyrePortfolio,contactQuery


def makelist(obj):
    lt = obj.split(";")
    ans = []
    for i in lt:
        i = i.replace('\r\n', "")
        if ':' in i:
            slt = i.split(':')
            ans.append(slt)
        else:
            ans.append(i)
    return ans

def home(request):
    home=homePage.objects.all()
    homeHero=homeHeroImage.objects.all()
    strengthInfo=strength.objects.all()
    blogs = blogPage.objects.all()
    products=homeProducts.objects.all()
    testimonials=testimonial.objects.all()
    return render(request,'index.html', {'home':home,'blogs': blogs,'homeHero':homeHero,'products':products,'testimonials':testimonials,'strengthInfo':strengthInfo})

def about(request):
    aboutInfo = aboutPage.objects.all()
    aboutMission = makelist(aboutInfo[0].mission)
    aboutVision = makelist(aboutInfo[0].vision)
    aboutCorporateValue = makelist(aboutInfo[0].corporateValue)
    teamInfo=team.objects.all()
    return render(request, 'about.html', {'about': aboutInfo, 'aboutMission': aboutMission, 'aboutVision': aboutVision, 'aboutCorporateValue': aboutCorporateValue,'teamInfo':teamInfo})
 

def contact(request):
    contactInfo = contactPage.objects.all()
    return render(request, 'contact.html', {'contact': contactInfo})

def clientele(request):
    clientele=clientelePage.objects.all()
    chemicalIndustry = chemicalPortfolio.objects.all()
    foodAndPharmaIndustries = foodPharmaPortfolio.objects.all()
    powerAndWindIndustry = powerWindPortfolio.objects.all()
    agrochemicalsIndustry = agrochemicalsPortfolio.objects.all()
    metalIndusty = metalPortfolio.objects.all()
    fertilizerIndustry = fertilizerPortfolio.objects.all()
    glassCeramicIndustry = glassCeramicPortfolio.objects.all()
    engieeringAutomobilesIndustry = engieeringAutomobilesPortfolio.objects.all()
    oilGasIndustry = oilGasPortfolio.objects.all()
    tyreIndustry = tyrePortfolio.objects.all()
    return render(request, 'clientele.html', {'clientele':clientele,'ci': chemicalIndustry, 'fpi': foodAndPharmaIndustries, 'pwi': powerAndWindIndustry, 'ai': agrochemicalsIndustry, 'mi': metalIndusty, 'fi': fertilizerIndustry, 'gci': glassCeramicIndustry, 'eai': engieeringAutomobilesIndustry, 'ogi': oilGasIndustry, 'ti': tyreIndustry})

def blogs(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    blogs = blogPage.objects.all().filter(blogTitle__icontains=search_query)
    blog=blogHero.objects.all()
    return render(request, 'blog.html', {'blogs': blogs,'blog':blog})

def servicess(request):
    serviceInfo=servicesPage.objects.all()
    valueAddedService = makelist(serviceInfo[0].addedServicesPoints)
    service=services.objects.all()
    return render(request,'services.html',{'service':service,'serviceInfo':serviceInfo,'valueAddedService':valueAddedService})

def products(request,pk):
    productName=pk
    mp=mechanicalProducts.objects.all()
    cp=civilProducts.objects.all()
    ep=electricalProducts.objects.all()
    maintananceProducts=otherMaintananceProducts.objects.all()
    mm=makelist(maintananceProducts[0].mechanicalMaintananceProducts)
    return render(request,'product.html',{'pk':pk,'mp':mp,'cp':cp,'ep':ep,'mm':mm})

def querySet(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobilenumber=request.POST.get('number')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        book, created = contactQuery.objects.get_or_create(name=name,email=email, mobilenumber=mobilenumber,subject=subject,message=message)
        book.save()
        return render(request,'index.html')

    