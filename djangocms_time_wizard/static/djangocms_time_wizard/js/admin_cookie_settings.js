$(document).ready(function () {
  $('#save').on('click', function (e) {
    const wrapper = $('#djangocms-time-wizard-cookie-settings')
    const values = []
    wrapper.find('input').each(function (index, item) {
      values.push(item.value + ":" + $(item).is(':checked').toString())
    })
    const cname = wrapper.data('cookie-name')
    const cvalue = values.join('::') + ';'
    const cpath = 'path=/;'
    document.cookie = cname + '=' + cvalue + cpath
  })
})
