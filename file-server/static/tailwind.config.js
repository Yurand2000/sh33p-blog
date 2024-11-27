tailwind.config = {
    darkMode: 'media',
    theme: {
      extend: {
        colors: {
          primary: tailwind.colors.teal,
          dark: {	50: '#F2F9F9',	100: '#B3D9D9',	200: '#73B9B9',	300: '#339999',	400: '#007A7A',	500: '#006A6A',	600: '#005B5B',	700: '#004C4C',	800: '#003C3C',	900: '#002D2D',	950: '#001D1D'},
          gray: tailwind.colors.stone
        }
      },
      fontFamily: {
        'body': [
      'Roboto', 
      'ui-sans-serif', 
      'system-ui', 
      '-apple-system', 
      'system-ui', 
      'Segoe UI', 
      'Roboto', 
      'Helvetica Neue', 
      'Arial', 
      'Noto Sans', 
      'sans-serif', 
      'Apple Color Emoji', 
      'Segoe UI Emoji', 
      'Segoe UI Symbol', 
      'Noto Color Emoji'
    ],
        'sans': [
      'Roboto', 
      'ui-sans-serif', 
      'system-ui', 
      '-apple-system', 
      'system-ui', 
      'Segoe UI', 
      'Roboto', 
      'Helvetica Neue', 
      'Arial', 
      'Noto Sans', 
      'sans-serif', 
      'Apple Color Emoji', 
      'Segoe UI Emoji', 
      'Segoe UI Symbol', 
      'Noto Color Emoji'
    ]
      }
    }
  }