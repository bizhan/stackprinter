if __name__ == '__main__':
    import time
    import sys
    import numpy as np
    from stackprinter import format

    class whatever():
        def ahoi(self):
            # raise Exception()
            return some_function('')

    outer_scope_thing = {'various': 'excellent',
                         123: 'things',
                         'in': np.ones((42,23))}

    def deco(f):
        bla = 1234
        def closure(*args, **kwargs):
            kwargs['things'] = bla
            return f(*args, **kwargs)

        return closure

    @deco
    def a_broken_function(thing,
                          various=None,
                          other=None,
                          things=None):
        """
        some very long
        doc string
        """
        bla = """ another triple quoted string """
        X = np.zeros((len(thing), len(outer_scope_thing)))
        X[0,0] = 1
        boing = outer_scope_thing['in']
        do_something = lambda val: another_broken_function(val + outer_scope_thing['in'] + boing)
        for k in X:
            if np.sum(k) != 0:
                # raise Exception()
                listcomp = [[do_something(val) for val in row] for row in X]

    def some_function(boing, zap='!'):
        thing = boing + zap
        a_broken_function(thing)


    def another_broken_function(val):
        if np.sum(val) != 42:
            bla = val.T.\
                  T.T.\
                  T
            # here is a comment \
            # that has backslashes \
            # for some reason
            ahoi = "here is a "\
                   "multi line "\
                   "string"

            # np.reshape(bla, 9000)
            boing = np.\
                    random.rand(*bla.T.\
                            T.T)
            raise Exception('something happened')


    # some_function("hello")
    # wha = whatever()
    # wha.ahoi()
    try:
        wha = whatever()
        wha.ahoi()
    except:
        stuff = sys.exc_info()
        scopidoped = 'gotcha'
        tic = time.perf_counter()

        msg = format(stuff, mode='plaintext', reverse=True, truncate_vals=500, suppressed_paths=["site-packages"])

        # took = time.perf_counter() - tic
        print(msg)
        # print('took', took * 1000)
