{
  'targets': [
    {
      'target_name': 'bigint',
      'sources': [ 'bigint.cc' ],
      'conditions': [
        ['OS=="linux"',
          {
            'link_settings': {
              'libraries': [
                '-lgmp'
              ]
            }
          }
        ],
        ['OS=="mac"',
          {
            'link_settings': {
              'libraries': [
                '-lgmp'
              ]
            }
          }
        ],
        ['OS=="win"',
          {
            'link_settings': {
              'libraries': [
                '-lgmp.lib'
              ],
            }
          }
        ],
        ['OS=="freebsd"',
          {
            'include_dirs': [
               '/usr/local/include'
             ],
             'libraries': [
               '/usr/local/lib'
             ],
            'link_settings': {
              'libraries': [
                '-lgmp'
              ],
            }
          }
        ]
      ]
    }
  ]
}
