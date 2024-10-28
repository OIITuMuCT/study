from plotly.offline import plot
import plotly.graph_objs as graphs

def user_profile(request):
    username = request.user.get_username()
    scatter_plot_html = scatter_plot_books_read(username)
    return render(requets, "user_profile.html", context={'plt_div': scatter_plot_html})