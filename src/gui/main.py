from appJar import gui

app = gui("htv-grabber", "800x400")

app.addLabel("title", "Welcome to appJar!")
app.setLabelBg("title", "red")

app.go()