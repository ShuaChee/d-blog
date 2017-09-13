# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_example_posts(apps, schema_editor):
    Post = apps.get_model('bb_post', 'Post')
    Post.objects.bulk_create([
        Post(
            subject='Volutpat sodales sed eleifend at feugiat ornare hendrerit curabitur.',
            content='''Parturient hac a eu cras parturient quisque turpis potenti a vitae in hendrerit maecenas vehicula scelerisque vehicula curae imperdiet fermentum rutrum senectus hac cum elit parturient. Nec semper nunc ridiculus phasellus suspendisse ante faucibus suspendisse nisl at hac scelerisque vestibulum ut senectus sem proin. A id magnis nam auctor commodo sed fusce inceptos maecenas a parturient amet lectus adipiscing justo duis aliquet sodales a.

Nam suspendisse sem parturient himenaeos vestibulum vestibulum ullamcorper suspendisse aliquet eu a adipiscing a sagittis a a a a ac urna ultrices mauris nec condimentum. Adipiscing a viverra consectetur parturient cursus ut non turpis sem vel sociis lorem netus hac a nam arcu mollis leo at vehicula nec venenatis a. A parturient primis justo vitae ad eget tristique amet a a non sed sed parturient id massa euismod gravida a.

Sociosqu fermentum suspendisse at ornare commodo eu imperdiet nibh scelerisque nec nisl duis mattis fames ac cras hac nunc adipiscing dictum massa. Non molestie vestibulum habitasse duis metus in a vulputate ullamcorper turpis nibh class luctus torquent dignissim rhoncus sem quis a. Vestibulum tincidunt maecenas nec senectus a magnis a erat fusce nam eu ante libero facilisi malesuada sociosqu ridiculus phasellus a accumsan orci lacus aptent. Parturient ad a in vestibulum a euismod a eget curae a in tellus ac risus in parturient class mus hendrerit parturient quis. Viverra ad litora eu a mi interdum vestibulum curae ad pretium parturient suscipit et nam adipiscing at a a dictumst id at litora ante imperdiet. Urna ac luctus viverra vulputate vestibulum blandit malesuada turpis vestibulum tellus ultrices suspendisse fames a phasellus a cum aenean habitant facilisis magna sed quis nisl molestie imperdiet vel suspendisse.'''
        ),
        Post(
            subject='Suspendisse a donec eget bibendum inceptos.',
            content='''Porttitor vehicula nisl himenaeos nibh dis ullamcorper consequat ullamcorper aliquet nunc condimentum aliquet dui aliquet dolor. Dis dui porta at fermentum odio non aliquam nisl volutpat ut turpis vitae lobortis turpis parturient ullamcorper mi ad velit vestibulum tortor suspendisse bibendum auctor justo. Ante scelerisque vulputate sagittis a commodo placerat parturient a arcu hendrerit himenaeos augue facilisis orci vestibulum erat placerat.

Et bibendum condimentum ullamcorper taciti neque a condimentum turpis sed parturient a eros libero condimentum pretium luctus pharetra amet a metus nisl facilisis quam nunc. Mi parturient purus sociosqu scelerisque in accumsan ullamcorper sed tortor nec lorem vehicula lacinia donec interdum nisi. Id ad diam platea quisque lectus a consectetur egestas sapien pharetra elit porttitor donec ac torquent lorem. Accumsan consectetur sed mus ridiculus imperdiet ac parturient dui facilisis consectetur sociosqu a nisi iaculis cum consectetur adipiscing blandit sodales interdum. Faucibus ullamcorper vitae euismod lorem scelerisque eu vestibulum ac a aliquam facilisi eu praesent accumsan nec in tempus consectetur eu ut vestibulum est himenaeos nibh. Sit tempus sit a hac a a suscipit scelerisque non nec maecenas praesent diam hac parturient adipiscing class praesent adipiscing ac duis nisl suspendisse ultricies interdum vestibulum montes.

Conubia habitant parturient vestibulum condimentum suspendisse sapien consectetur quam quis tincidunt vel proin leo ridiculus scelerisque dolor inceptos dis pharetra vestibulum. Sed adipiscing facilisi in aenean adipiscing condimentum proin elementum scelerisque felis nam massa a adipiscing taciti suspendisse sit hac scelerisque sociosqu. Donec eget himenaeos imperdiet suspendisse erat penatibus dolor parturient feugiat nulla suspendisse tellus nam torquent vestibulum praesent a sapien.

A a nascetur a elit class odio parturient dictumst venenatis penatibus malesuada neque metus primis quam nulla inceptos neque mi non sagittis. A lectus aliquet a praesent at a malesuada ac himenaeos magna faucibus posuere quam erat parturient dolor sodales. Vehicula scelerisque leo morbi cum hendrerit cras magnis adipiscing volutpat nisi adipiscing enim placerat ullamcorper faucibus varius. Condimentum aptent fringilla a a enim mi vestibulum parturient elit nec lacinia erat curabitur feugiat parturient vivamus elementum aenean tincidunt natoque mus consectetur malesuada sem hendrerit consectetur suspendisse.

A ante posuere tristique suspendisse suspendisse gravida ullamcorper dis consectetur dis a quisque suspendisse malesuada felis a egestas ullamcorper proin iaculis massa vivamus dui primis vivamus. Diam lacus condimentum vitae montes consequat scelerisque dictumst venenatis a sapien ullamcorper a ligula ultrices. A eu eleifend vivamus consequat condimentum hac fermentum nibh ullamcorper sem parturient potenti a platea suspendisse consectetur id adipiscing dolor. Nunc enim laoreet tristique tellus aliquet nullam nullam a a scelerisque vestibulum et nascetur urna a nam ullamcorper hendrerit mauris suspendisse consectetur duis ullamcorper a dictumst a venenatis.

Egestas eros elit ut non nam adipiscing tellus adipiscing tristique at condimentum cras amet euismod nec enim dui id dis scelerisque suspendisse non a volutpat. At leo gravida scelerisque ullamcorper mollis vulputate nibh amet nascetur feugiat a suspendisse dis suspendisse eu urna a a vivamus sed parturient curabitur. Quis ullamcorper sociosqu sodales eu class a imperdiet aenean risus phasellus lectus vestibulum est nam venenatis primis suspendisse tincidunt ultrices ad at. Porta maecenas venenatis a non eu vestibulum pharetra faucibus nec elit venenatis turpis inceptos senectus leo praesent in accumsan lobortis ullamcorper eu condimentum. Sodales suspendisse felis condimentum mi adipiscing per penatibus fames sed vestibulum a ad tincidunt a sociosqu mus venenatis sem a ridiculus vestibulum. Egestas dis semper fusce convallis parturient mus adipiscing commodo scelerisque potenti aenean amet nibh convallis condimentum et scelerisque eget.

Per maecenas erat a habitant tempor a aliquam hac consectetur auctor vestibulum parturient hendrerit conubia habitasse nec natoque parturient vulputate consectetur non. A volutpat elementum semper id pharetra nisl proin amet vel scelerisque felis mi nisl condimentum conubia mus inceptos laoreet dapibus. A vel condimentum sagittis sem vitae fames egestas imperdiet praesent adipiscing a porta hac ullamcorper facilisis habitant scelerisque ad a senectus a. Pretium risus sociosqu scelerisque eget consequat tortor eu aliquam mi eu pharetra parturient condimentum erat semper posuere diam cum. Sodales consectetur enim dignissim purus adipiscing condimentum nullam ut a nisl scelerisque phasellus platea congue sodales senectus ullamcorper suspendisse blandit porta feugiat sem a eu mauris bibendum. Ut ac urna vulputate condimentum eget vestibulum vel morbi a netus netus duis adipiscing enim vestibulum.'''
        ),
        Post(
            subject='Consectetur ullamcorper.',
            content='''Dapibus suspendisse mus facilisis euismod varius eu accumsan eget pulvinar consectetur mus a parturient cursus ullamcorper phasellus feugiat erat magna tincidunt vitae vulputate. Egestas erat condimentum tincidunt primis facilisi condimentum cubilia porttitor auctor a nisl parturient parturient himenaeos a parturient habitasse himenaeos. Scelerisque laoreet a ullamcorper feugiat a sem eros imperdiet fringilla litora aptent integer egestas curabitur est ultricies mus mi in phasellus ullamcorper nam.

Bibendum netus consectetur nec lobortis augue a suspendisse suscipit sociosqu id accumsan dictum a parturient tempor montes pharetra ullamcorper rhoncus lorem pretium. Accumsan elit litora ridiculus nam dis vestibulum tincidunt iaculis cras amet scelerisque litora a augue vestibulum parturient adipiscing et integer sociosqu massa non parturient vestibulum erat luctus adipiscing. Ad rutrum venenatis venenatis sem eu in nullam torquent cursus facilisis morbi natoque euismod vestibulum ipsum. Id vel parturient suspendisse parturient placerat scelerisque rhoncus parturient a a maecenas pretium mi placerat nam a accumsan sociis torquent integer.

Morbi curae sociis felis a curae laoreet nunc parturient habitasse mi ultrices vestibulum nunc ultrices vitae non ullamcorper proin vestibulum elit sodales id condimentum suscipit fermentum vestibulum suspendisse. Ut odio velit rhoncus himenaeos elit ullamcorper a lacinia odio vestibulum vestibulum ornare a mi condimentum senectus. Fusce parturient arcu a consequat tempus mattis scelerisque nec vitae nam magna vestibulum nisi auctor in ridiculus. Ultrices blandit parturient a suspendisse dui diam magnis egestas molestie adipiscing vel primis parturient id condimentum scelerisque euismod enim congue. Sociosqu sagittis tristique ut litora libero vestibulum ullamcorper consequat leo vestibulum vestibulum nulla ac ad. Odio dui purus ridiculus condimentum natoque molestie scelerisque ipsum etiam quam scelerisque a lobortis commodo commodo netus sociis ullamcorper dui a.

Sem sed dignissim sem justo libero sit hac mauris phasellus tincidunt consectetur ipsum primis elementum a a etiam a donec ullamcorper a malesuada molestie tristique dui facilisi nisi. Vestibulum proin scelerisque amet fermentum sem libero turpis a ullamcorper ridiculus tempor elit vestibulum a curabitur malesuada urna vitae consectetur donec vulputate nibh nullam phasellus a litora parturient lacus. Parturient consectetur adipiscing eu mi mus volutpat mi nec adipiscing phasellus etiam egestas tincidunt lorem pulvinar a bibendum ac. Leo luctus nunc vestibulum scelerisque a ullamcorper sem tincidunt varius convallis per orci aptent ad sit.'''
        )
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('bb_post', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_example_posts)
    ]
