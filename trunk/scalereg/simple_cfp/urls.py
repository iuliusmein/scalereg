from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'scalereg.simple_cfp.views.index'),
    (r'^recover_validation/$', 'scalereg.simple_cfp.views.RecoverValidation'),
    (r'^speaker_registration/$', 'scalereg.simple_cfp.views.RegisterSpeaker'),
    (r'^submit_presentation/$', 'scalereg.simple_cfp.views.SubmitPresentation'),
)