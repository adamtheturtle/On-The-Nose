import web
import os

urls = (
    '/', 'index',
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
    def GET(self):
        directory = os.listdir('static/nose_images/')
        nose_images = [file[:-5] for file in directory if file[-5:] == '.jpeg']
        noses = [(nose.split(',')[0], nose.split(',')[1])
                 for nose in nose_images if ',' in nose]

        return render.index(noses=noses)

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
