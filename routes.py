import cherrypy
from views.view import ViewBHAVCopy


class BhavCopy(object):

    @cherrypy.expose
    def companies(self, company_name=None):
        view = ViewBHAVCopy()
        if company_name:
            return "".join(view.get_by_name_view(company_name))

        return "".join(view.get_top_ten_view())
