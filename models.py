from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class homePage(models.Model):
    homePageAbout=models.TextField(max_length=10000,blank=False,null=False)
    homePageAboutImage=models.ImageField(default="1.png")
    homeTestimonialBackground=models.CharField(max_length=10000,blank=False,null=False)
    homeStrengthBackground=models.CharField(max_length=10000,blank=False,null=True)
    
class homeProducts(models.Model):
    mechanicalProductImage=models.ImageField(default="1.png")
    civilProductImage=models.ImageField(default="1.png")
    electricalProductImage=models.ImageField(default="1.png")
    mechanicalProductImageDescription=models.CharField(max_length=10000,blank=False,null=True)
    civilProductImageDescription=models.CharField(max_length=10000,blank=False,null=False)
    electricalProductImageDescription=models.CharField(max_length=10000,blank=False,null=False)
    mechanicalProductDescription=models.TextField(max_length=10000,blank=False,null=True)
    civilProductDescription=models.TextField(max_length=10000,blank=False,null=True)
    electricalProductDescription=models.TextField(max_length=10000,blank=False,null=True)

class strength(models.Model):
    homeOurStrengthIcon=models.CharField(max_length=10000,blank=False,null=False)
    homeOurStrengthHeading=models.CharField(max_length=10000,blank=False,null=True)
    homeOurStrengthText=models.CharField(max_length=10000,blank=False,null=False)
    homeOurStrengthCard=models.CharField(max_length=300,blank=False,null=False,default="strength-card")

class testimonial(models.Model):
    homeTestimonialImage=models.ImageField(default="2.png")
    homeTestimonialAuthor =models.TextField(max_length=200,blank=False,null=True)
    homeTestimonialDesignation=models.CharField(max_length=200,blank=False,null=True)
    homeTestimonialContent=models.CharField(max_length=2000,blank=False,null=True)
   
class homeHeroImage(models.Model):
    homeHeroImage=models.CharField(max_length=10000,blank=False,null=False)
    homeHeroImageHeading=models.TextField(max_length=10000,blank=False,null=False)
    homeHeroImageContent=models.TextField(max_length=10000,blank=False,null=False)

class contactPage(models.Model):
    heroImageLink=models.CharField(max_length=10000,blank=False,null=False)
    address=models.TextField(max_length=10000,blank=False,null=False)
    contact=models.CharField(max_length=10000,blank=False,null=False)
    email=models.EmailField(max_length=200,blank=False,null=False)
    formImageLink=models.CharField(max_length=10000,blank=False,null=True)

class contactQuery(models.Model):
    name = models.CharField(blank=False,null=False,max_length=200)
    mobilenumber = models.CharField(blank=False,null=False,max_length=1000)
    email = models.CharField(blank=False,null=False,max_length=200)
    subject = models.CharField(blank=False,null=False,max_length=200)
    message = models.CharField(blank=False,null=False,max_length=2000)
    def __str__(self):
        return self.name + 'Query'

class clientelePage(models.Model):
    heroImageLink=models.CharField(max_length=10000,blank=False,null=False)

class chemicalPortfolio(models.Model):
    title=models.CharField(max_length=200,null=False,blank=False)
    order=models.SmallIntegerField(blank=False,null=False)
    image=models.ImageField(blank=False,null=False,default="logo.png")

    def __str__(self):
        return self.title

class foodPharmaPortfolio(models.Model):
    title=models.CharField(max_length=200,null=False,blank=False)
    order=models.SmallIntegerField(blank=False,null=False)
    image=models.ImageField(blank=False,null=False,default="logo.png")

    def __str__(self):
        return self.title

class powerWindPortfolio(models.Model):
    title=models.CharField(max_length=200,null=False,blank=False)
    order=models.SmallIntegerField(blank=False,null=False)
    image=models.ImageField(blank=False,null=False,default="logo.png")

    def __str__(self):
        return self.title

class agrochemicalsPortfolio(models.Model):
    title=models.CharField(max_length=200,null=False,blank=False)
    order=models.SmallIntegerField(blank=False,null=False)
    image=models.ImageField(blank=False,null=False,default="logo.png")

    def __str__(self):
        return self.title

class metalPortfolio(models.Model):
    title=models.CharField(max_length=200,null=False,blank=False)
    order=models.SmallIntegerField(blank=False,null=False)
    image=models.ImageField(blank=False,null=False,default="logo.png")

    def __str__(self):
        return self.title

class fertilizerPortfolio(models.Model):
    title=models.CharField(max_length=200,null=False,blank=False)
    order=models.SmallIntegerField(blank=False,null=False)
    image=models.ImageField(blank=False,null=False,default="logo.png")

    def __str__(self):
        return self.title

class glassCeramicPortfolio(models.Model):
    title=models.CharField(max_length=200,null=False,blank=False)
    order=models.SmallIntegerField(blank=False,null=False)
    image=models.ImageField(blank=False,null=False,default="logo.png")

    def __str__(self):
        return self.title

class engieeringAutomobilesPortfolio(models.Model):
    title=models.CharField(max_length=200,null=False,blank=False)
    order=models.SmallIntegerField(blank=False,null=False)
    image=models.ImageField(blank=False,null=False,default="logo.png")

    def __str__(self):
        return self.title

class oilGasPortfolio(models.Model):
    title=models.CharField(max_length=200,null=False,blank=False)
    order=models.SmallIntegerField(blank=False,null=False)
    image=models.ImageField(blank=False,null=False,default="logo.png")

    def __str__(self):
        return self.title

class tyrePortfolio(models.Model):
    title=models.CharField(max_length=200,null=False,blank=False)
    order=models.SmallIntegerField(blank=False,null=False)
    image=models.ImageField(blank=False,null=False,default="logo.png")

    def __str__(self):
        return self.title

class blogHero(models.Model):
    heroImageLink=models.CharField(max_length=10000,blank=False,null=True)

class blogPage(models.Model):
    blogTitle=models.CharField(max_length=2000,blank=False,null=False)
    blogAuthor=models.CharField(max_length=200,blank=False,null=False)
    blogDate=models.CharField(max_length=200,blank=False,null=False)
    blogContent=models.TextField(max_length=20000,blank=False,null=False)
    blogImage=models.CharField(max_length=2000,blank=False,null=False)
    
class aboutPage(models.Model):
    heroimageLink=models.CharField(max_length=3000,blank=False,null=False)
    aboutParagraph=models.TextField(max_length=5000,blank=False,null=False)
    aboutParagraphImage=models.ImageField(default="logo.png")
    companyEstablishedYear=models.CharField(max_length=200,blank=False,null=False)
    companyEmployees=models.CharField(max_length=2000,blank=False,null=False)
    companyProjects=models.CharField(max_length=2000,blank=False,null=False)
    companyAnnualTurnover=models.CharField(max_length=2000,blank=False,null=False)
    vision=models.CharField(max_length=5000,blank=False,null=False,help_text="Enter ; After every Mission Point i.e abc;bcd")
    mission=models.CharField(max_length=5000,blank=False,null=False,help_text="Enter ; After every Mission Point i.e abc;bcd")
    corporateValue=models.CharField(max_length=5000,blank=False,null=False,help_text="Enter ; After every Mission Point i.e abc;bcd")
    missionvissionBackground=models.TextField(max_length=3000,blank=False,null=False)
    clientBackground=models.TextField(max_length=3000,blank=False,null=False)
    companyValuesBackground=models.TextField(max_length=3000,blank=False,null=False)
    teamBackground=models.TextField(max_length=3000,blank=False,null=False)
    

class team(models.Model):
    teamMemberImage=models.CharField(max_length=2000,blank=False,null=False)
    teamMemberName=models.CharField(max_length=200,blank=False,null=False)
    teamMemberDesignation=models.CharField(max_length=200,blank=False,null=False)

class servicesPage(models.Model):
    heroimageLink=models.CharField(max_length=3000,blank=False,null=False)
    addedServicesPoints=models.CharField(max_length=10000,blank=False,null=False,help_text="Enter ; After every Mission Point i.e abc;bcd")
    servicesOneImage=models.CharField(max_length=2000,blank=False,null=False)
    servicesTwoImage=models.CharField(max_length=2000,blank=False,null=True)
    servicesThreeImage=models.CharField(max_length=2000,blank=False,null=True)


class services(models.Model):
    servicesImage=models.CharField(max_length=2000,blank=False,null=False)
    servicesIcon=models.CharField(max_length=200,blank=False,null=False)
    servicesName=models.CharField(max_length=200,blank=False,null=False)
    servicesInfo=models.TextField(max_length=3000,blank=False,null=False)

class mechanicalProducts(models.Model):
    mechanicalProductImage=models.ImageField(default="logo.png")
    mechanicalProductImageName=models.CharField(max_length=2000,blank=False,null=False)
    mechanicalProductsImageDescription=models.TextField(max_length=2000,blank=True,null=True)

class civilProducts(models.Model):
    civilProductImage=models.ImageField(default="logo.png")
    civilProductImageName=models.CharField(max_length=2000,blank=False,null=False)
    civilProductsImageDescription=models.TextField(max_length=2000,blank=True,null=True)

class electricalProducts(models.Model):
    electricalProductImage=models.ImageField(default="logo.png")
    electricalProductImageName=models.CharField(max_length=2000,blank=False,null=False)
    electricalProductsImageDescription=models.TextField(max_length=2000,blank=True,null=True)

class otherMaintananceProducts(models.Model):
    mechanicalMaintananceProducts=models.TextField(max_length=2000,blank=True,null=True)