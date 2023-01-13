from pytest_bdd import scenario, given, when, then


@given("eu clico2")
def step_impl():
    raise NotImplementedError(u'STEP: Given eu clico2')


@when("vou3")
def step_impl():
    raise NotImplementedError(u'STEP: When vou3')


@then("tela3")
def step_impl():
    raise NotImplementedError(u'STEP: Then tela3')