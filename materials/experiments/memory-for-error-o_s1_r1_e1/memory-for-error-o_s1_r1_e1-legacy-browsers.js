/************************************ 
 * Memory-For-Error-O_S1_R1_E1 Test *
 ************************************/


// store info about the experiment session:
let expName = 'memory-for-error-o_s1_r1_e1';  // from the Builder filename that created this script
let expInfo = {'id': '', 'cb': ["A", "B"], 'friendly': ["A", "B"]};

// Start code blocks for 'Before Experiment'
// for our own functions we need these specified in the global space 
// so these are defined in the "Before experiment" tab
// linspace (this will be used in place of numpy.linspace for picking ISI)


var n;
function linspace(a,b,n) {
    if(typeof n === "undefined") n = Math.max(Math.round(b-a)+1,1);
    if(n<2) { return n===1?[a]:[]; }
    var i,ret = Array(n);
    n--;
    for(i=n;i>=0;i--) { ret[i] = (i*b+(n-i)*a)/n; }
    return ret;
}
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('0.5000, 0.5000, 0.5000'),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(JS_codeRoutineBegin());
flowScheduler.add(JS_codeRoutineEachFrame());
flowScheduler.add(JS_codeRoutineEnd());
flowScheduler.add(setupRoutineBegin());
flowScheduler.add(setupRoutineEachFrame());
flowScheduler.add(setupRoutineEnd());
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(instructRightRoutineBegin());
flowScheduler.add(instructRightRoutineEachFrame());
flowScheduler.add(instructRightRoutineEnd());
flowScheduler.add(instructLeftRoutineBegin());
flowScheduler.add(instructLeftRoutineEachFrame());
flowScheduler.add(instructLeftRoutineEnd());
flowScheduler.add(instructInconRightRoutineBegin());
flowScheduler.add(instructInconRightRoutineEachFrame());
flowScheduler.add(instructInconRightRoutineEnd());
flowScheduler.add(instructInconLeftRoutineBegin());
flowScheduler.add(instructInconLeftRoutineEachFrame());
flowScheduler.add(instructInconLeftRoutineEnd());
const prac_block_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_block_loopLoopBegin(prac_block_loopLoopScheduler));
flowScheduler.add(prac_block_loopLoopScheduler);
flowScheduler.add(prac_block_loopLoopEnd);
const task_block_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(task_block_loopLoopBegin(task_block_loopLoopScheduler));
flowScheduler.add(task_block_loopLoopScheduler);
flowScheduler.add(task_block_loopLoopEnd);
flowScheduler.add(fixation1RoutineBegin());
flowScheduler.add(fixation1RoutineEachFrame());
flowScheduler.add(fixation1RoutineEnd());
flowScheduler.add(errorNumbers_2RoutineBegin());
flowScheduler.add(errorNumbers_2RoutineEachFrame());
flowScheduler.add(errorNumbers_2RoutineEnd());
flowScheduler.add(botherRateRoutineBegin());
flowScheduler.add(botherRateRoutineEachFrame());
flowScheduler.add(botherRateRoutineEnd());
flowScheduler.add(askExperimenterRoutineBegin());
flowScheduler.add(askExperimenterRoutineEachFrame());
flowScheduler.add(askExperimenterRoutineEnd());
flowScheduler.add(surpriseInstructRoutineBegin());
flowScheduler.add(surpriseInstructRoutineEachFrame());
flowScheduler.add(surpriseInstructRoutineEnd());
const surprise_block_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(surprise_block_loopLoopBegin(surprise_block_loopLoopScheduler));
flowScheduler.add(surprise_block_loopLoopScheduler);
flowScheduler.add(surprise_block_loopLoopEnd);
flowScheduler.add(friendlyInstruct1RoutineBegin());
flowScheduler.add(friendlyInstruct1RoutineEachFrame());
flowScheduler.add(friendlyInstruct1RoutineEnd());
const friendly_block_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(friendly_block_loopLoopBegin(friendly_block_loopLoopScheduler));
flowScheduler.add(friendly_block_loopLoopScheduler);
flowScheduler.add(friendly_block_loopLoopEnd);
flowScheduler.add(finishMessageRoutineBegin());
flowScheduler.add(finishMessageRoutineEachFrame());
flowScheduler.add(finishMessageRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'img/neutralC/CFD-AM-220-134-N.jpg', 'path': 'img/neutralC/CFD-AM-220-134-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-226-095-N.jpg', 'path': 'img/neutralC/CFD-WF-226-095-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-647-548-N.jpg', 'path': 'img/neutralC/CFD-IM-647-548-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-046-006-N.jpg', 'path': 'img/neutralC/CFD-BM-046-006-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-329-001-N.jpg', 'path': 'img/neutralC/CFD-MF-329-001-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-206-045-N.jpg', 'path': 'img/neutralC/CFD-WM-206-045-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-204-189-N.jpg', 'path': 'img/neutralC/CFD-BF-204-189-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-233-106-N.jpg', 'path': 'img/neutralC/CFD-WM-233-106-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-207-014-N.jpg', 'path': 'img/neutralC/CFD-WF-207-014-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-674-281-N.jpg', 'path': 'img/neutralC/CFD-IM-674-281-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-715-013-N.jpg', 'path': 'img/neutralC/CFD-IM-715-013-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-246-087-N.jpg', 'path': 'img/neutralC/CFD-LM-246-087-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-712-005-N.jpg', 'path': 'img/neutralC/CFD-IM-712-005-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-244-197-N.jpg', 'path': 'img/neutralC/CFD-BM-244-197-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-210-086-N.jpg', 'path': 'img/neutralC/CFD-WF-210-086-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-255-140-N.jpg', 'path': 'img/neutralC/CFD-BF-255-140-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-359-019-N.jpg', 'path': 'img/neutralC/CFD-MF-359-019-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-248-149-N.jpg', 'path': 'img/neutralC/CFD-BF-248-149-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-623-129-N.jpg', 'path': 'img/neutralC/CFD-IF-623-129-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-209-038-N.jpg', 'path': 'img/neutralC/CFD-WM-209-038-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-050-003-N.jpg', 'path': 'img/neutralC/CFD-BF-050-003-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-205-001-N.jpg', 'path': 'img/neutralC/CFD-BM-205-001-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-016-036-N.jpg', 'path': 'img/neutralC/CFD-BM-016-036-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-228-125-N.jpg', 'path': 'img/neutralC/CFD-LF-228-125-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-633-012-N.jpg', 'path': 'img/neutralC/CFD-IF-633-012-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-324-031-N.jpg', 'path': 'img/neutralC/CFD-MF-324-031-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-224-197-N.jpg', 'path': 'img/neutralC/CFD-WM-224-197-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-013-001-N.jpg', 'path': 'img/neutralC/CFD-BF-013-001-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-215-145-N.jpg', 'path': 'img/neutralC/CFD-WF-215-145-N.jpg'},
    {'name': 'a_halfV_friendlyTable2.csv', 'path': 'a_halfV_friendlyTable2.csv'},
    {'name': 'img/neutralC/CFD-BM-039-029-N.jpg', 'path': 'img/neutralC/CFD-BM-039-029-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-634-382-N.jpg', 'path': 'img/neutralC/CFD-IF-634-382-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-240-206-N.jpg', 'path': 'img/neutralC/CFD-AF-240-206-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-216-079-N.jpg', 'path': 'img/neutralC/CFD-WF-216-079-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-225-192-N.jpg', 'path': 'img/neutralC/CFD-BF-225-192-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-250-149-N.jpg', 'path': 'img/neutralC/CFD-AM-250-149-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-233-171-N.jpg', 'path': 'img/neutralC/CFD-LM-233-171-N.jpg'},
    {'name': 'a_halfV_trialTable_2.csv', 'path': 'a_halfV_trialTable_2.csv'},
    {'name': 'img/neutralC/CFD-MF-300-002-N.jpg', 'path': 'img/neutralC/CFD-MF-300-002-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-229-004-N.jpg', 'path': 'img/neutralC/CFD-WF-229-004-N.jpg'},
    {'name': 'a_halfV_surpriseTable2.csv', 'path': 'a_halfV_surpriseTable2.csv'},
    {'name': 'img/neutralC/CFD-AM-244-222-N.jpg', 'path': 'img/neutralC/CFD-AM-244-222-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-002-013-N.jpg', 'path': 'img/neutralC/CFD-BM-002-013-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-206-114-N.jpg', 'path': 'img/neutralC/CFD-BM-206-114-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-729-393-N.jpg', 'path': 'img/neutralC/CFD-IF-729-393-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-231-357-N.jpg', 'path': 'img/neutralC/CFD-AF-231-357-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-306-003-N.jpg', 'path': 'img/neutralC/CFD-MF-306-003-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-203-001-N.jpg', 'path': 'img/neutralC/CFD-BM-203-001-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-332-014-N.jpg', 'path': 'img/neutralC/CFD-MF-332-014-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-034-031-N.jpg', 'path': 'img/neutralC/CFD-BM-034-031-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-042-026-N.jpg', 'path': 'img/neutralC/CFD-BF-042-026-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-028-003-N.jpg', 'path': 'img/neutralC/CFD-WM-028-003-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-215-120-N.jpg', 'path': 'img/neutralC/CFD-AM-215-120-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-248-104-N.jpg', 'path': 'img/neutralC/CFD-AM-248-104-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-655-234-N.jpg', 'path': 'img/neutralC/CFD-IM-655-234-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-323-053-N.jpg', 'path': 'img/neutralC/CFD-MM-323-053-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-001-025-N.jpg', 'path': 'img/neutralC/CFD-BF-001-025-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-202-072-N.jpg', 'path': 'img/neutralC/CFD-LM-202-072-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-227-054-N.jpg', 'path': 'img/neutralC/CFD-LF-227-054-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-214-168-N.jpg', 'path': 'img/neutralC/CFD-AM-214-168-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-324-069-N.jpg', 'path': 'img/neutralC/CFD-MM-324-069-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-239-148-N.jpg', 'path': 'img/neutralC/CFD-LF-239-148-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-204-122-N.jpg', 'path': 'img/neutralC/CFD-AM-204-122-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-688-322-N.jpg', 'path': 'img/neutralC/CFD-IM-688-322-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-692-011-N.jpg', 'path': 'img/neutralC/CFD-IM-692-011-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-218-087-N.jpg', 'path': 'img/neutralC/CFD-WF-218-087-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-209-006-N.jpg', 'path': 'img/neutralC/CFD-AF-209-006-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-250-167-N.jpg', 'path': 'img/neutralC/CFD-WF-250-167-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-234-176-N.jpg', 'path': 'img/neutralC/CFD-LM-234-176-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-250-170-N.jpg', 'path': 'img/neutralC/CFD-BM-250-170-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-020-002-N.jpg', 'path': 'img/neutralC/CFD-BF-020-002-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-620-218-N.jpg', 'path': 'img/neutralC/CFD-IF-620-218-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-252-191-N.jpg', 'path': 'img/neutralC/CFD-BF-252-191-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-213-031-N.jpg', 'path': 'img/neutralC/CFD-WF-213-031-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-219-101-N.jpg', 'path': 'img/neutralC/CFD-AM-219-101-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-021-013-N.jpg', 'path': 'img/neutralC/CFD-BF-021-013-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-230-202-N.jpg', 'path': 'img/neutralC/CFD-LM-230-202-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-230-158-N.jpg', 'path': 'img/neutralC/CFD-WF-230-158-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-229-164-N.jpg', 'path': 'img/neutralC/CFD-LF-229-164-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-238-154-N.jpg', 'path': 'img/neutralC/CFD-LF-238-154-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-236-107-N.jpg', 'path': 'img/neutralC/CFD-WF-236-107-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-215-177-N.jpg', 'path': 'img/neutralC/CFD-BF-215-177-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-243-170-N.jpg', 'path': 'img/neutralC/CFD-AF-243-170-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-003-003-N.jpg', 'path': 'img/neutralC/CFD-BM-003-003-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-033-003-N.jpg', 'path': 'img/neutralC/CFD-BM-033-003-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-699-002-N.jpg', 'path': 'img/neutralC/CFD-IM-699-002-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-211-168-N.jpg', 'path': 'img/neutralC/CFD-BF-211-168-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-700-009-N.jpg', 'path': 'img/neutralC/CFD-IM-700-009-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-206-086-N.jpg', 'path': 'img/neutralC/CFD-AM-206-086-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-207-004-N.jpg', 'path': 'img/neutralC/CFD-BF-207-004-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-251-014-N.jpg', 'path': 'img/neutralC/CFD-WF-251-014-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-245-166-N.jpg', 'path': 'img/neutralC/CFD-LF-245-166-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-023-010-N.jpg', 'path': 'img/neutralC/CFD-BF-023-010-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-246-192-N.jpg', 'path': 'img/neutralC/CFD-BM-246-192-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-616-214-N.jpg', 'path': 'img/neutralC/CFD-IM-616-214-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-238-023-N.jpg', 'path': 'img/neutralC/CFD-WF-238-023-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-336-016-N.jpg', 'path': 'img/neutralC/CFD-MF-336-016-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-676-017-N.jpg', 'path': 'img/neutralC/CFD-IF-676-017-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-304-018-N.jpg', 'path': 'img/neutralC/CFD-MF-304-018-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-024-003-N.jpg', 'path': 'img/neutralC/CFD-WF-024-003-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-213-061-N.jpg', 'path': 'img/neutralC/CFD-LM-213-061-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-664-651-N.jpg', 'path': 'img/neutralC/CFD-IM-664-651-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-720-014-N.jpg', 'path': 'img/neutralC/CFD-IM-720-014-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-251-057-N.jpg', 'path': 'img/neutralC/CFD-LF-251-057-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-648-337-N.jpg', 'path': 'img/neutralC/CFD-IM-648-337-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-232-251-N.jpg', 'path': 'img/neutralC/CFD-AM-232-251-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-022-017-N.jpg', 'path': 'img/neutralC/CFD-WF-022-017-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-327-002-N.jpg', 'path': 'img/neutralC/CFD-MF-327-002-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-208-127-N.jpg', 'path': 'img/neutralC/CFD-LF-208-127-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-245-164-N.jpg', 'path': 'img/neutralC/CFD-BM-245-164-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-220-068-N.jpg', 'path': 'img/neutralC/CFD-WM-220-068-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-631-363-N.jpg', 'path': 'img/neutralC/CFD-IF-631-363-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-231-260-N.jpg', 'path': 'img/neutralC/CFD-LF-231-260-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-011-002-N.jpg', 'path': 'img/neutralC/CFD-WM-011-002-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-013-002-N.jpg', 'path': 'img/neutralC/CFD-BM-013-002-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-051-035-N.jpg', 'path': 'img/neutralC/CFD-BF-051-035-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-689-263-N.jpg', 'path': 'img/neutralC/CFD-IM-689-263-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-023-003-N.jpg', 'path': 'img/neutralC/CFD-WF-023-003-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-641-504-N.jpg', 'path': 'img/neutralC/CFD-IF-641-504-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-224-176-N.jpg', 'path': 'img/neutralC/CFD-LF-224-176-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-224-126-N.jpg', 'path': 'img/neutralC/CFD-AM-224-126-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-211-128-N.jpg', 'path': 'img/neutralC/CFD-LM-211-128-N.jpg'},
    {'name': 'a_halfV_trialTable_3.csv', 'path': 'a_halfV_trialTable_3.csv'},
    {'name': 'a_halfV_surpriseTable1.csv', 'path': 'a_halfV_surpriseTable1.csv'},
    {'name': 'img/neutralC/CFD-IM-663-230-N.jpg', 'path': 'img/neutralC/CFD-IM-663-230-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-210-035-N.jpg', 'path': 'img/neutralC/CFD-AM-210-035-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-017-003-N.jpg', 'path': 'img/neutralC/CFD-WF-017-003-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-228-212-N.jpg', 'path': 'img/neutralC/CFD-BF-228-212-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-035-032-N.jpg', 'path': 'img/neutralC/CFD-WM-035-032-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-673-389-N.jpg', 'path': 'img/neutralC/CFD-IF-673-389-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-346-008-N.jpg', 'path': 'img/neutralC/CFD-MF-346-008-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-205-141-N.jpg', 'path': 'img/neutralC/CFD-BF-205-141-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-659-359-N.jpg', 'path': 'img/neutralC/CFD-IM-659-359-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-201-057-N.jpg', 'path': 'img/neutralC/CFD-LM-201-057-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-706-002-N.jpg', 'path': 'img/neutralC/CFD-IM-706-002-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-300-035-N.jpg', 'path': 'img/neutralC/CFD-MM-300-035-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-205-007-N.jpg', 'path': 'img/neutralC/CFD-WM-205-007-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-315-013-N.jpg', 'path': 'img/neutralC/CFD-MM-315-013-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-033-025-N.jpg', 'path': 'img/neutralC/CFD-WM-033-025-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-707-105-N.jpg', 'path': 'img/neutralC/CFD-IM-707-105-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-242-011-N.jpg', 'path': 'img/neutralC/CFD-WM-242-011-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-242-001-N.jpg', 'path': 'img/neutralC/CFD-WF-242-001-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-207-048-N.jpg', 'path': 'img/neutralC/CFD-WM-207-048-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-216-121-N.jpg', 'path': 'img/neutralC/CFD-LF-216-121-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-041-001-N.jpg', 'path': 'img/neutralC/CFD-BF-041-001-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-019-002-N.jpg', 'path': 'img/neutralC/CFD-BM-019-002-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-348-018-N.jpg', 'path': 'img/neutralC/CFD-MF-348-018-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-239-171-N.jpg', 'path': 'img/neutralC/CFD-AF-239-171-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-014-002-N.jpg', 'path': 'img/neutralC/CFD-BF-014-002-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-049-032-N.jpg', 'path': 'img/neutralC/CFD-BF-049-032-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-026-002-N.jpg', 'path': 'img/neutralC/CFD-BM-026-002-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-677-452-1-N.jpg', 'path': 'img/neutralC/CFD-IF-677-452-1-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-242-176-N.jpg', 'path': 'img/neutralC/CFD-AM-242-176-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-691-007-N.jpg', 'path': 'img/neutralC/CFD-IF-691-007-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-014-002-N.jpg', 'path': 'img/neutralC/CFD-WM-014-002-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-034-006-N.jpg', 'path': 'img/neutralC/CFD-WF-034-006-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-247-051-N.jpg', 'path': 'img/neutralC/CFD-LF-247-051-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-236-163-N.jpg', 'path': 'img/neutralC/CFD-LM-236-163-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-713-170-N.jpg', 'path': 'img/neutralC/CFD-IF-713-170-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-001-014-N.jpg', 'path': 'img/neutralC/CFD-BM-001-014-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-214-308-N.jpg', 'path': 'img/neutralC/CFD-BF-214-308-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-687-511-N.jpg', 'path': 'img/neutralC/CFD-IM-687-511-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-241-222-N.jpg', 'path': 'img/neutralC/CFD-BF-241-222-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-695-001-N.jpg', 'path': 'img/neutralC/CFD-IM-695-001-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-236-177-N.jpg', 'path': 'img/neutralC/CFD-BF-236-177-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-209-072-N.jpg', 'path': 'img/neutralC/CFD-LF-209-072-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-022-001-N.jpg', 'path': 'img/neutralC/CFD-WM-022-001-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-220-120-N.jpg', 'path': 'img/neutralC/CFD-LF-220-120-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-345-025-N.jpg', 'path': 'img/neutralC/CFD-MF-345-025-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-256-160-N.jpg', 'path': 'img/neutralC/CFD-AF-256-160-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-251-211-N.jpg', 'path': 'img/neutralC/CFD-BF-251-211-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-622-096-N.jpg', 'path': 'img/neutralC/CFD-IF-622-096-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-213-079-N.jpg', 'path': 'img/neutralC/CFD-LF-213-079-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-253-130-N.jpg', 'path': 'img/neutralC/CFD-AF-253-130-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-230-131-N.jpg', 'path': 'img/neutralC/CFD-WM-230-131-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-221-147-N.jpg', 'path': 'img/neutralC/CFD-AF-221-147-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-219-106-N.jpg', 'path': 'img/neutralC/CFD-AF-219-106-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-221-223-N.jpg', 'path': 'img/neutralC/CFD-BF-221-223-N.jpg'},
    {'name': 'img/leftArrow.png', 'path': 'img/leftArrow.png'},
    {'name': 'img/neutralC/CFD-BF-008-001-N.jpg', 'path': 'img/neutralC/CFD-BF-008-001-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-022-022-N.jpg', 'path': 'img/neutralC/CFD-BM-022-022-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-015-015-N.jpg', 'path': 'img/neutralC/CFD-BM-015-015-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-220-329-N.jpg', 'path': 'img/neutralC/CFD-LM-220-329-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-224-002-N.jpg', 'path': 'img/neutralC/CFD-BF-224-002-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-231-155-N.jpg', 'path': 'img/neutralC/CFD-BM-231-155-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-249-163-N.jpg', 'path': 'img/neutralC/CFD-AM-249-163-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-006-017-N.jpg', 'path': 'img/neutralC/CFD-BF-006-017-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-230-232-N.jpg', 'path': 'img/neutralC/CFD-BM-230-232-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-301-024-N.jpg', 'path': 'img/neutralC/CFD-MF-301-024-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-254-167-N.jpg', 'path': 'img/neutralC/CFD-AF-254-167-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-228-065-N.jpg', 'path': 'img/neutralC/CFD-WM-228-065-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-338-001-N.jpg', 'path': 'img/neutralC/CFD-MF-338-001-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-319-016-N.jpg', 'path': 'img/neutralC/CFD-MF-319-016-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-240-013-N.jpg', 'path': 'img/neutralC/CFD-LM-240-013-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-014-002-N.jpg', 'path': 'img/neutralC/CFD-WF-014-002-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-027-003-N.jpg', 'path': 'img/neutralC/CFD-WF-027-003-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-240-207-N.jpg', 'path': 'img/neutralC/CFD-BM-240-207-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-232-078-N.jpg', 'path': 'img/neutralC/CFD-AF-232-078-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-040-003-N.jpg', 'path': 'img/neutralC/CFD-BF-040-003-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-311-001-N.jpg', 'path': 'img/neutralC/CFD-MM-311-001-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-335-002-N.jpg', 'path': 'img/neutralC/CFD-MF-335-002-N.jpg'},
    {'name': 'a_halfV_trialTable_practice.csv', 'path': 'a_halfV_trialTable_practice.csv'},
    {'name': 'img/neutralC/CFD-BF-206-143-N.jpg', 'path': 'img/neutralC/CFD-BF-206-143-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-214-139-N.jpg', 'path': 'img/neutralC/CFD-AF-214-139-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-010-003-N.jpg', 'path': 'img/neutralC/CFD-BM-010-003-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-223-250-N.jpg', 'path': 'img/neutralC/CFD-BF-223-250-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-033-028-N.jpg', 'path': 'img/neutralC/CFD-BF-033-028-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-666-372-N.jpg', 'path': 'img/neutralC/CFD-IM-666-372-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-037-022-N.jpg', 'path': 'img/neutralC/CFD-BF-037-022-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-216-114-N.jpg', 'path': 'img/neutralC/CFD-AM-216-114-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-201-156-N.jpg', 'path': 'img/neutralC/CFD-WF-201-156-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-214-165-N.jpg', 'path': 'img/neutralC/CFD-LM-214-165-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-323-001-N.jpg', 'path': 'img/neutralC/CFD-MF-323-001-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-333-012-N.jpg', 'path': 'img/neutralC/CFD-MF-333-012-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-357-002-N.jpg', 'path': 'img/neutralC/CFD-MF-357-002-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-226-234-N.jpg', 'path': 'img/neutralC/CFD-AM-226-234-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-026-002-N.jpg', 'path': 'img/neutralC/CFD-WF-026-002-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-203-184-N.jpg', 'path': 'img/neutralC/CFD-BF-203-184-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-223-138-N.jpg', 'path': 'img/neutralC/CFD-AM-223-138-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-241-235-N.jpg', 'path': 'img/neutralC/CFD-BM-241-235-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-223-183-N.jpg', 'path': 'img/neutralC/CFD-AF-223-183-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-228-214-N.jpg', 'path': 'img/neutralC/CFD-AM-228-214-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-003-003-N.jpg', 'path': 'img/neutralC/CFD-BF-003-003-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-033-002-N.jpg', 'path': 'img/neutralC/CFD-WF-033-002-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-694-297-N.jpg', 'path': 'img/neutralC/CFD-IM-694-297-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-201-060-N.jpg', 'path': 'img/neutralC/CFD-AF-201-060-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-249-235-N.jpg', 'path': 'img/neutralC/CFD-BM-249-235-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-233-190-N.jpg', 'path': 'img/neutralC/CFD-AF-233-190-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-029-002-N.jpg', 'path': 'img/neutralC/CFD-WF-029-002-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-015-004-N.jpg', 'path': 'img/neutralC/CFD-BF-015-004-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-025-035-N.jpg', 'path': 'img/neutralC/CFD-BM-025-035-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-048-002-N.jpg', 'path': 'img/neutralC/CFD-BF-048-002-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-241-287-N.jpg', 'path': 'img/neutralC/CFD-AM-241-287-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-334-002-N.jpg', 'path': 'img/neutralC/CFD-MF-334-002-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-206-079-N.jpg', 'path': 'img/neutralC/CFD-AF-206-079-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-030-002-N.jpg', 'path': 'img/neutralC/CFD-WF-030-002-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-315-002-N.jpg', 'path': 'img/neutralC/CFD-MF-315-002-N.jpg'},
    {'name': 'a_halfV_trialTable_10.csv', 'path': 'a_halfV_trialTable_10.csv'},
    {'name': 'img/neutralC/CFD-LM-224-162-N.jpg', 'path': 'img/neutralC/CFD-LM-224-162-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-008-002-N.jpg', 'path': 'img/neutralC/CFD-WF-008-002-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-233-277-N.jpg', 'path': 'img/neutralC/CFD-LF-233-277-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-344-012-N.jpg', 'path': 'img/neutralC/CFD-MF-344-012-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-231-202-N.jpg', 'path': 'img/neutralC/CFD-BF-231-202-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-030-003-N.jpg', 'path': 'img/neutralC/CFD-BM-030-003-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-617-174-N.jpg', 'path': 'img/neutralC/CFD-IM-617-174-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-235-226-N.jpg', 'path': 'img/neutralC/CFD-BM-235-226-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-235-241-N.jpg', 'path': 'img/neutralC/CFD-AM-235-241-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-240-083-N.jpg', 'path': 'img/neutralC/CFD-WF-240-083-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-703-182-N.jpg', 'path': 'img/neutralC/CFD-IM-703-182-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-230-203-N.jpg', 'path': 'img/neutralC/CFD-LF-230-203-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-210-156-N.jpg', 'path': 'img/neutralC/CFD-LM-210-156-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-017-021-N.jpg', 'path': 'img/neutralC/CFD-BM-017-021-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-681-253-N.jpg', 'path': 'img/neutralC/CFD-IM-681-253-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-018-001-N.jpg', 'path': 'img/neutralC/CFD-BM-018-001-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-212-050-N.jpg', 'path': 'img/neutralC/CFD-WF-212-050-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-235-170-N.jpg', 'path': 'img/neutralC/CFD-AF-235-170-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-216-061-N.jpg', 'path': 'img/neutralC/CFD-WM-216-061-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-609-408-N.jpg', 'path': 'img/neutralC/CFD-IF-609-408-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-029-031-N.jpg', 'path': 'img/neutralC/CFD-BF-029-031-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-243-107-N.jpg', 'path': 'img/neutralC/CFD-WM-243-107-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-225-102-N.jpg', 'path': 'img/neutralC/CFD-AM-225-102-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-305-003-N.jpg', 'path': 'img/neutralC/CFD-MM-305-003-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-221-216-N.jpg', 'path': 'img/neutralC/CFD-LM-221-216-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-356-017-N.jpg', 'path': 'img/neutralC/CFD-MF-356-017-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-678-482-N.jpg', 'path': 'img/neutralC/CFD-IM-678-482-N.jpg'},
    {'name': 'a_halfV_trialTable_9.csv', 'path': 'a_halfV_trialTable_9.csv'},
    {'name': 'img/neutralC/CFD-WF-249-126-N.jpg', 'path': 'img/neutralC/CFD-WF-249-126-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-693-172-N.jpg', 'path': 'img/neutralC/CFD-IF-693-172-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-243-212-N.jpg', 'path': 'img/neutralC/CFD-AM-243-212-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-215-70-N.jpg', 'path': 'img/neutralC/CFD-AF-215-70-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-233-236-N.jpg', 'path': 'img/neutralC/CFD-AM-233-236-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-219-141-N.jpg', 'path': 'img/neutralC/CFD-BM-219-141-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-247-165-N.jpg', 'path': 'img/neutralC/CFD-AM-247-165-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-249-239-N.jpg', 'path': 'img/neutralC/CFD-WM-249-239-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-690-282-N.jpg', 'path': 'img/neutralC/CFD-IM-690-282-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-034-030-N.jpg', 'path': 'img/neutralC/CFD-WM-034-030-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-230-189-N.jpg', 'path': 'img/neutralC/CFD-BF-230-189-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-645-001-N.jpg', 'path': 'img/neutralC/CFD-IM-645-001-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-234-172-N.jpg', 'path': 'img/neutralC/CFD-BM-234-172-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-238-185-N.jpg', 'path': 'img/neutralC/CFD-AF-238-185-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-009-001-N.jpg', 'path': 'img/neutralC/CFD-WF-009-001-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-742-103-N.jpg', 'path': 'img/neutralC/CFD-IF-742-103-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-605-066-N.jpg', 'path': 'img/neutralC/CFD-IF-605-066-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-218-157-N.jpg', 'path': 'img/neutralC/CFD-AF-218-157-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-236-221-N.jpg', 'path': 'img/neutralC/CFD-LF-236-221-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-245-178-N.jpg', 'path': 'img/neutralC/CFD-BF-245-178-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-735-353-N.jpg', 'path': 'img/neutralC/CFD-IF-735-353-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-317-002-N.jpg', 'path': 'img/neutralC/CFD-MF-317-002-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-301-011-N.jpg', 'path': 'img/neutralC/CFD-MM-301-011-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-342-022-N.jpg', 'path': 'img/neutralC/CFD-MF-342-022-N.jpg'},
    {'name': 'img/rightArrow.png', 'path': 'img/rightArrow.png'},
    {'name': 'img/neutralC/CFD-IM-621-136-N.jpg', 'path': 'img/neutralC/CFD-IM-621-136-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-710-016-N.jpg', 'path': 'img/neutralC/CFD-IF-710-016-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-013-003-N.jpg', 'path': 'img/neutralC/CFD-WF-013-003-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-212-066-N.jpg', 'path': 'img/neutralC/CFD-LF-212-066-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-239-147-N.jpg', 'path': 'img/neutralC/CFD-AM-239-147-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-639-263-N.jpg', 'path': 'img/neutralC/CFD-IM-639-263-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-230-193-N.jpg', 'path': 'img/neutralC/CFD-AF-230-193-N.jpg'},
    {'name': 'a_halfV_trialTable_5.csv', 'path': 'a_halfV_trialTable_5.csv'},
    {'name': 'img/neutralC/CFD-MF-316-001-N.jpg', 'path': 'img/neutralC/CFD-MF-316-001-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-217-082-N.jpg', 'path': 'img/neutralC/CFD-LF-217-082-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-028-001-N.jpg', 'path': 'img/neutralC/CFD-BF-028-001-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-227-184-N.jpg', 'path': 'img/neutralC/CFD-AM-227-184-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-027-001-N.jpg', 'path': 'img/neutralC/CFD-BM-027-001-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-016-001-N.jpg', 'path': 'img/neutralC/CFD-WM-016-001-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-238-190-N.jpg', 'path': 'img/neutralC/CFD-BF-238-190-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-222-240-N.jpg', 'path': 'img/neutralC/CFD-BF-222-240-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-013-001-N.jpg', 'path': 'img/neutralC/CFD-WM-013-001-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-237-067-N.jpg', 'path': 'img/neutralC/CFD-WF-237-067-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-234-355-N.jpg', 'path': 'img/neutralC/CFD-AM-234-355-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-207-023-N.jpg', 'path': 'img/neutralC/CFD-AF-207-023-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-702-101-N.jpg', 'path': 'img/neutralC/CFD-IM-702-101-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-047-003-N.jpg', 'path': 'img/neutralC/CFD-BF-047-003-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-011-016-N.jpg', 'path': 'img/neutralC/CFD-BM-011-016-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-656-273-N.jpg', 'path': 'img/neutralC/CFD-IM-656-273-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-214-026-N.jpg', 'path': 'img/neutralC/CFD-WM-214-026-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-602-134-N.jpg', 'path': 'img/neutralC/CFD-IF-602-134-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-229-224-N.jpg', 'path': 'img/neutralC/CFD-AM-229-224-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-244-168-N.jpg', 'path': 'img/neutralC/CFD-AF-244-168-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-252-135-N.jpg', 'path': 'img/neutralC/CFD-AF-252-135-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-204-067-N.jpg', 'path': 'img/neutralC/CFD-AF-204-067-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-204-001-N.jpg', 'path': 'img/neutralC/CFD-LM-204-001-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-244-231-N.jpg', 'path': 'img/neutralC/CFD-BF-244-231-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-331-010-N.jpg', 'path': 'img/neutralC/CFD-MF-331-010-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-225-154-N.jpg', 'path': 'img/neutralC/CFD-BM-225-154-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-019-001-N.jpg', 'path': 'img/neutralC/CFD-BF-019-001-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-208-110-N.jpg', 'path': 'img/neutralC/CFD-LM-208-110-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-246-242-N.jpg', 'path': 'img/neutralC/CFD-AF-246-242-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-242-158-N.jpg', 'path': 'img/neutralC/CFD-AF-242-158-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-221-005-N.jpg', 'path': 'img/neutralC/CFD-WF-221-005-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-241-210-N.jpg', 'path': 'img/neutralC/CFD-WF-241-210-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-212-097-N.jpg', 'path': 'img/neutralC/CFD-WM-212-097-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-237-172-N.jpg', 'path': 'img/neutralC/CFD-BF-237-172-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-003-002-N.jpg', 'path': 'img/neutralC/CFD-WM-003-002-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-201-076-N.jpg', 'path': 'img/neutralC/CFD-AM-201-076-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-203-077-N.jpg', 'path': 'img/neutralC/CFD-AF-203-077-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-667-369-N.jpg', 'path': 'img/neutralC/CFD-IM-667-369-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-215-247-N.jpg', 'path': 'img/neutralC/CFD-LM-215-247-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-340-026-N.jpg', 'path': 'img/neutralC/CFD-MF-340-026-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-232-199-N.jpg', 'path': 'img/neutralC/CFD-LF-232-199-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-244-003-N.jpg', 'path': 'img/neutralC/CFD-WM-244-003-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-248-089-N.jpg', 'path': 'img/neutralC/CFD-LM-248-089-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-726-248-N.jpg', 'path': 'img/neutralC/CFD-IM-726-248-N.jpg'},
    {'name': 'a_halfV_trialTable_1.csv', 'path': 'a_halfV_trialTable_1.csv'},
    {'name': 'img/neutralC/CFD-WF-016-015-N.jpg', 'path': 'img/neutralC/CFD-WF-016-015-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-227-002-N.jpg', 'path': 'img/neutralC/CFD-WF-227-002-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-226-174-N.jpg', 'path': 'img/neutralC/CFD-LF-226-174-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-233-116-N.jpg', 'path': 'img/neutralC/CFD-BF-233-116-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-037-025-N.jpg', 'path': 'img/neutralC/CFD-WM-037-025-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-001-014-N.jpg', 'path': 'img/neutralC/CFD-WM-001-014-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-660-464-N.jpg', 'path': 'img/neutralC/CFD-IF-660-464-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-250-157-N.jpg', 'path': 'img/neutralC/CFD-WM-250-157-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-044-034-N.jpg', 'path': 'img/neutralC/CFD-BF-044-034-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-009-002-N.jpg', 'path': 'img/neutralC/CFD-BM-009-002-N.jpg'},
    {'name': 'friendlyBlock_select_A.xlsx', 'path': 'friendlyBlock_select_A.xlsx'},
    {'name': 'img/neutralC/CFD-LM-238-129-N.jpg', 'path': 'img/neutralC/CFD-LM-238-129-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-714-008-1-N.jpg', 'path': 'img/neutralC/CFD-IF-714-008-1-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-242-121-N.jpg', 'path': 'img/neutralC/CFD-LF-242-121-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-211-001-N.jpg', 'path': 'img/neutralC/CFD-WF-211-001-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-252-114-N.jpg', 'path': 'img/neutralC/CFD-AM-252-114-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-240-191-N.jpg', 'path': 'img/neutralC/CFD-AM-240-191-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-209-172-N.jpg', 'path': 'img/neutralC/CFD-BF-209-172-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-653-008-N.jpg', 'path': 'img/neutralC/CFD-IM-653-008-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-322-002-N.jpg', 'path': 'img/neutralC/CFD-MM-322-002-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-221-184-N.jpg', 'path': 'img/neutralC/CFD-AM-221-184-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-029-023-N.jpg', 'path': 'img/neutralC/CFD-WM-029-023-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-016-017-N.jpg', 'path': 'img/neutralC/CFD-BF-016-017-N.jpg'},
    {'name': 'friendlyBlock_select_B.xlsx', 'path': 'friendlyBlock_select_B.xlsx'},
    {'name': 'img/neutralC/CFD-IF-601-519-N.jpg', 'path': 'img/neutralC/CFD-IF-601-519-N.jpg'},
    {'name': 'img/cover_background.png', 'path': 'img/cover_background.png'},
    {'name': 'img/neutralC/CFD-WM-239-128-N.jpg', 'path': 'img/neutralC/CFD-WM-239-128-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-208-003-N.jpg', 'path': 'img/neutralC/CFD-AF-208-003-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-679-069-N.jpg', 'path': 'img/neutralC/CFD-IM-679-069-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-310-001-N.jpg', 'path': 'img/neutralC/CFD-MM-310-001-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-043-071-N.jpg', 'path': 'img/neutralC/CFD-BM-043-071-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-644-306-1-N.jpg', 'path': 'img/neutralC/CFD-IF-644-306-1-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-200-099-N.jpg', 'path': 'img/neutralC/CFD-WF-200-099-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-234-086-N.jpg', 'path': 'img/neutralC/CFD-WF-234-086-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-223-056-N.jpg', 'path': 'img/neutralC/CFD-WM-223-056-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-043-003-N.jpg', 'path': 'img/neutralC/CFD-BF-043-003-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-012-018-N.jpg', 'path': 'img/neutralC/CFD-BM-012-018-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-302-002-N.jpg', 'path': 'img/neutralC/CFD-MM-302-002-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-200-080-N.jpg', 'path': 'img/neutralC/CFD-BF-200-080-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-325-002-N.jpg', 'path': 'img/neutralC/CFD-MF-325-002-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-200-046-N.jpg', 'path': 'img/neutralC/CFD-BM-200-046-N.jpg'},
    {'name': 'a_halfV_trialTable_4.csv', 'path': 'a_halfV_trialTable_4.csv'},
    {'name': 'img/neutralC/CFD-BF-212-315-N.jpg', 'path': 'img/neutralC/CFD-BF-212-315-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-612-149-N.jpg', 'path': 'img/neutralC/CFD-IF-612-149-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-743-006-N.jpg', 'path': 'img/neutralC/CFD-IM-743-006-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-258-125-N.jpg', 'path': 'img/neutralC/CFD-WM-258-125-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-221-198-N.jpg', 'path': 'img/neutralC/CFD-BM-221-198-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-232-161-N.jpg', 'path': 'img/neutralC/CFD-WF-232-161-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-625-225-N.jpg', 'path': 'img/neutralC/CFD-IF-625-225-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-024-001-N.jpg', 'path': 'img/neutralC/CFD-BM-024-001-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-246-170-N.jpg', 'path': 'img/neutralC/CFD-BF-246-170-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-246-184-N.jpg', 'path': 'img/neutralC/CFD-AM-246-184-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-214-090-N.jpg', 'path': 'img/neutralC/CFD-LF-214-090-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-204-038-N.jpg', 'path': 'img/neutralC/CFD-WF-204-038-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-238-020-N.jpg', 'path': 'img/neutralC/CFD-WM-238-020-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-651-308-N.jpg', 'path': 'img/neutralC/CFD-IM-651-308-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-039-018-N.jpg', 'path': 'img/neutralC/CFD-WM-039-018-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-239-136-N.jpg', 'path': 'img/neutralC/CFD-BM-239-136-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-347-001-N.jpg', 'path': 'img/neutralC/CFD-MF-347-001-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-684-008-N.jpg', 'path': 'img/neutralC/CFD-IM-684-008-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-207-004-N.jpg', 'path': 'img/neutralC/CFD-LM-207-004-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-021-021-N.jpg', 'path': 'img/neutralC/CFD-BM-021-021-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-234-208-N.jpg', 'path': 'img/neutralC/CFD-AF-234-208-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-034-002-N.jpg', 'path': 'img/neutralC/CFD-BF-034-002-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-204-133-N.jpg', 'path': 'img/neutralC/CFD-LF-204-133-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-218-132-N.jpg', 'path': 'img/neutralC/CFD-BM-218-132-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-041-035-N.jpg', 'path': 'img/neutralC/CFD-BM-041-035-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-330-001-N.jpg', 'path': 'img/neutralC/CFD-MF-330-001-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-307-002-N.jpg', 'path': 'img/neutralC/CFD-MM-307-002-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-722-456-N.jpg', 'path': 'img/neutralC/CFD-IF-722-456-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-251-002-N.jpg', 'path': 'img/neutralC/CFD-WM-251-002-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-248-129-N.jpg', 'path': 'img/neutralC/CFD-WF-248-129-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-235-121-N.jpg', 'path': 'img/neutralC/CFD-WF-235-121-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-205-100-N.jpg', 'path': 'img/neutralC/CFD-LF-205-100-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-629-234-N.jpg', 'path': 'img/neutralC/CFD-IF-629-234-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-209-048-N.jpg', 'path': 'img/neutralC/CFD-AM-209-048-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-203-023-N.jpg', 'path': 'img/neutralC/CFD-WM-203-023-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-208-068-N.jpg', 'path': 'img/neutralC/CFD-WF-208-068-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-719-221-N.jpg', 'path': 'img/neutralC/CFD-IM-719-221-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-011-002-N.jpg', 'path': 'img/neutralC/CFD-BF-011-002-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-321-003-N.jpg', 'path': 'img/neutralC/CFD-MF-321-003-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-744-114-N.jpg', 'path': 'img/neutralC/CFD-IF-744-114-N.jpg'},
    {'name': 'blockSelect.csv', 'path': 'blockSelect.csv'},
    {'name': 'blockSelect_practice.csv', 'path': 'blockSelect_practice.csv'},
    {'name': 'img/neutralC/CFD-IM-709-103-N.jpg', 'path': 'img/neutralC/CFD-IM-709-103-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-237-188-N.jpg', 'path': 'img/neutralC/CFD-BM-237-188-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-228-173-N.jpg', 'path': 'img/neutralC/CFD-AF-228-173-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-237-052-N.jpg', 'path': 'img/neutralC/CFD-WM-237-052-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-302-027-N.jpg', 'path': 'img/neutralC/CFD-MF-302-027-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-306-010-N.jpg', 'path': 'img/neutralC/CFD-MM-306-010-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-727-195-N.jpg', 'path': 'img/neutralC/CFD-IM-727-195-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-219-038-N.jpg', 'path': 'img/neutralC/CFD-WF-219-038-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-009-002-N.jpg', 'path': 'img/neutralC/CFD-BF-009-002-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-036-023-N.jpg', 'path': 'img/neutralC/CFD-WF-036-023-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-225-101-N.jpg', 'path': 'img/neutralC/CFD-WF-225-101-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-231-136-N.jpg', 'path': 'img/neutralC/CFD-AM-231-136-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-303-002-N.jpg', 'path': 'img/neutralC/CFD-MM-303-002-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-305-014-N.jpg', 'path': 'img/neutralC/CFD-MF-305-014-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-253-202-N.jpg', 'path': 'img/neutralC/CFD-BF-253-202-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-027-002-N.jpg', 'path': 'img/neutralC/CFD-BF-027-002-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-210-050-N.jpg', 'path': 'img/neutralC/CFD-AF-210-050-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-316-156-N.jpg', 'path': 'img/neutralC/CFD-MM-316-156-N.jpg'},
    {'name': 'a_halfV_trialTable_6.csv', 'path': 'a_halfV_trialTable_6.csv'},
    {'name': 'img/neutralC/CFD-IM-654-417-N.jpg', 'path': 'img/neutralC/CFD-IM-654-417-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-211-054-N.jpg', 'path': 'img/neutralC/CFD-WM-211-054-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-661-254-N.jpg', 'path': 'img/neutralC/CFD-IM-661-254-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-221-002-N.jpg', 'path': 'img/neutralC/CFD-LF-221-002-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-731-223-N.jpg', 'path': 'img/neutralC/CFD-IM-731-223-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-230-150-N.jpg', 'path': 'img/neutralC/CFD-AM-230-150-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-314-062-N.jpg', 'path': 'img/neutralC/CFD-MM-314-062-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-734-108-N.jpg', 'path': 'img/neutralC/CFD-IF-734-108-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-222-239-N.jpg', 'path': 'img/neutralC/CFD-LM-222-239-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-003-003-N.jpg', 'path': 'img/neutralC/CFD-WF-003-003-N.jpg'},
    {'name': 'img/neutralC/CFD-IF-732-260-N.jpg', 'path': 'img/neutralC/CFD-IF-732-260-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-728-041-N.jpg', 'path': 'img/neutralC/CFD-IM-728-041-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-208-266-N.jpg', 'path': 'img/neutralC/CFD-BF-208-266-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-303-013-N.jpg', 'path': 'img/neutralC/CFD-MF-303-013-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-308-001-N.jpg', 'path': 'img/neutralC/CFD-MF-308-001-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-211-052-N.jpg', 'path': 'img/neutralC/CFD-AM-211-052-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-245-123-N.jpg', 'path': 'img/neutralC/CFD-WM-245-123-N.jpg'},
    {'name': 'surpriseBlock_select_B.xlsx', 'path': 'surpriseBlock_select_B.xlsx'},
    {'name': 'img/neutralC/CFD-IM-683-231-N.jpg', 'path': 'img/neutralC/CFD-IM-683-231-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-226-251-N.jpg', 'path': 'img/neutralC/CFD-AF-226-251-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-040-002-N.jpg', 'path': 'img/neutralC/CFD-BM-040-002-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-226-119-N.jpg', 'path': 'img/neutralC/CFD-BF-226-119-N.jpg'},
    {'name': 'img/neutralC/CFD-MM-319-052-N.jpg', 'path': 'img/neutralC/CFD-MM-319-052-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-007-001-N.jpg', 'path': 'img/neutralC/CFD-WF-007-001-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-234-118-N.jpg', 'path': 'img/neutralC/CFD-WM-234-118-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-239-075-N.jpg', 'path': 'img/neutralC/CFD-LM-239-075-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-339-002-N.jpg', 'path': 'img/neutralC/CFD-MF-339-002-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-652-191-N.jpg', 'path': 'img/neutralC/CFD-IM-652-191-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-227-207-N.jpg', 'path': 'img/neutralC/CFD-AF-227-207-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-005-003-N.jpg', 'path': 'img/neutralC/CFD-BM-005-003-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-233-285-N.jpg', 'path': 'img/neutralC/CFD-BM-233-285-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-247-095-N.jpg', 'path': 'img/neutralC/CFD-LM-247-095-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-630-134-N.jpg', 'path': 'img/neutralC/CFD-IM-630-134-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-021-001-N.jpg', 'path': 'img/neutralC/CFD-WM-021-001-N.jpg'},
    {'name': 'a_halfV_trialTable_8.csv', 'path': 'a_halfV_trialTable_8.csv'},
    {'name': 'img/neutralC/CFD-WM-256-138-N.jpg', 'path': 'img/neutralC/CFD-WM-256-138-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-214-075-N.jpg', 'path': 'img/neutralC/CFD-BM-214-075-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-219-295-N.jpg', 'path': 'img/neutralC/CFD-LM-219-295-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-343-001-N.jpg', 'path': 'img/neutralC/CFD-MF-343-001-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-238-269-N.jpg', 'path': 'img/neutralC/CFD-AM-238-269-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-217-162-N.jpg', 'path': 'img/neutralC/CFD-LM-217-162-N.jpg'},
    {'name': 'surpriseBlock_select_A.xlsx', 'path': 'surpriseBlock_select_A.xlsx'},
    {'name': 'img/neutralC/CFD-IM-716-316-N.jpg', 'path': 'img/neutralC/CFD-IM-716-316-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-226-276-N.jpg', 'path': 'img/neutralC/CFD-BM-226-276-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-229-129-N.jpg', 'path': 'img/neutralC/CFD-WM-229-129-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-222-173-N.jpg', 'path': 'img/neutralC/CFD-BM-222-173-N.jpg'},
    {'name': 'img/transp_fixation.png', 'path': 'img/transp_fixation.png'},
    {'name': 'img/neutralC/CFD-BF-250-121-N.jpg', 'path': 'img/neutralC/CFD-BF-250-121-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-023-029-N.jpg', 'path': 'img/neutralC/CFD-BM-023-029-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-032-024-N.jpg', 'path': 'img/neutralC/CFD-BM-032-024-N.jpg'},
    {'name': 'img/neutralC/CFD-AF-212-097-N.jpg', 'path': 'img/neutralC/CFD-AF-212-097-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-236-090-N.jpg', 'path': 'img/neutralC/CFD-AM-236-090-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-216-082-N.jpg', 'path': 'img/neutralC/CFD-LM-216-082-N.jpg'},
    {'name': 'img/neutralC/CFD-BF-005-001-N.jpg', 'path': 'img/neutralC/CFD-BF-005-001-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-310-027-N.jpg', 'path': 'img/neutralC/CFD-MF-310-027-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-218-074-N.jpg', 'path': 'img/neutralC/CFD-WM-218-074-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-354-067-N.jpg', 'path': 'img/neutralC/CFD-MF-354-067-N.jpg'},
    {'name': 'a_halfV_friendlyTable1.csv', 'path': 'a_halfV_friendlyTable1.csv'},
    {'name': 'img/neutralC/CFD-IF-704-125-N.jpg', 'path': 'img/neutralC/CFD-IF-704-125-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-208-065-N.jpg', 'path': 'img/neutralC/CFD-BM-208-065-N.jpg'},
    {'name': 'a_halfV_trialTable_7.csv', 'path': 'a_halfV_trialTable_7.csv'},
    {'name': 'img/neutralC/CFD-IM-603-305-N.jpg', 'path': 'img/neutralC/CFD-IM-603-305-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-222-057-N.jpg', 'path': 'img/neutralC/CFD-WM-222-057-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-213-134-N.jpg', 'path': 'img/neutralC/CFD-BM-213-134-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-215-155-N.jpg', 'path': 'img/neutralC/CFD-BM-215-155-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-232-204-N.jpg', 'path': 'img/neutralC/CFD-LM-232-204-N.jpg'},
    {'name': 'img/neutralC/CFD-MF-326-016-N.jpg', 'path': 'img/neutralC/CFD-MF-326-016-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-229-187-N.jpg', 'path': 'img/neutralC/CFD-LM-229-187-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-698-011-N.jpg', 'path': 'img/neutralC/CFD-IM-698-011-N.jpg'},
    {'name': 'img/neutralC/CFD-WM-012-001-N.jpg', 'path': 'img/neutralC/CFD-WM-012-001-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-637-007-N.jpg', 'path': 'img/neutralC/CFD-IM-637-007-N.jpg'},
    {'name': 'img/neutralC/CFD-LF-240-199-N.jpg', 'path': 'img/neutralC/CFD-LF-240-199-N.jpg'},
    {'name': 'img/neutralC/CFD-LM-235-231-N.jpg', 'path': 'img/neutralC/CFD-LM-235-231-N.jpg'},
    {'name': 'img/neutralC/CFD-WF-021-002-N.jpg', 'path': 'img/neutralC/CFD-WF-021-002-N.jpg'},
    {'name': 'img/neutralC/CFD-IM-736-361-N.jpg', 'path': 'img/neutralC/CFD-IM-736-361-N.jpg'},
    {'name': 'img/neutralC/CFD-BM-204-003-N.jpg', 'path': 'img/neutralC/CFD-BM-204-003-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-245-111-N.jpg', 'path': 'img/neutralC/CFD-AM-245-111-N.jpg'},
    {'name': 'img/neutralC/CFD-AM-251-124-N.jpg', 'path': 'img/neutralC/CFD-AM-251-124-N.jpg'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.1.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["id"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var JS_codeClock;
var shuffle;
var setupClock;
var welcomeClock;
var welcome_text;
var welcome_keyResp;
var instructRightClock;
var instructRight_text;
var instructRight_centerImg;
var instructRight_rightImg1;
var instructRight_leftImg1;
var insructRight_keyResp;
var instructLeftClock;
var instructLeft_text;
var instructLeft_centerImg;
var instructLeft_rightImg1;
var instructLeft_leftImg1;
var instructLeft_keyResp;
var instructInconRightClock;
var instructInconRight_text;
var instructIncon_centerImg;
var instructIncon_rightImg1;
var instructIncon_leftImg1;
var insructInconRight_keyResp;
var instructInconLeftClock;
var instructInconLeft_text;
var instructInconLeft_centerImg;
var instructInconLeft_rightImg1;
var instructInconLeft_leftImg1;
var instructInconLeft_keyResp;
var prac_blockRemindersClock;
var trialNum;
var accuracy;
var numCorr;
var blockAcc;
var prac_blockText;
var prac_reminder_text;
var prac_reminder_keyResp;
var initFixationClock;
var initFixation_img;
var prac_stimRoutineClock;
var thisISI;
var bigFace;
var cover_background_2;
var prac_centerImg;
var prac_rightImg1;
var prac_rightImg2;
var prac_leftImg1;
var prac_leftImg2;
var prac_fixImg;
var prac_stim_keyResp;
var prac_blockFeedClock;
var prac_blockFeed_text;
var prac_pressContinue;
var prac_blockFeed_keyResp;
var task_blockRemindersClock;
var blockCounter;
var task_blockText;
var task_blockReminders_text;
var task_blockReminders_keyResp;
var task_stimRoutineClock;
var bigFace_2;
var cover_background;
var task_centerImg;
var task_rightImg1;
var task_rightImg2;
var task_leftImg1;
var task_leftImg2;
var task_fixImg;
var task1_stim_keyResp;
var task_blockFeedClock;
var task_blockFeed_text;
var task_blockFeed_text2;
var task_blockFeed_keyResp;
var fixation1Clock;
var fix;
var errorNumbers_2Clock;
var errorNumbers_text_2;
var textbox_2;
var errorN_key_resp_2;
var botherRateClock;
var botherRate_text;
var textbox_3;
var botherRate_key_resp;
var askExperimenterClock;
var surpriseInstructClock;
var instruct_surprise1;
var instruct_surp1_key_resp;
var instructSurpriseTask2_2Clock;
var instructMainTask_text;
var instructMainTask_keyResp;
var surpriseTaskClock;
var stimulus;
var instructsurpA1_right;
var instructsurpA2_left;
var surprise_key_resp;
var friendlyInstruct1Clock;
var instruct_surprise1_2;
var instruct_surp1_key_resp_2;
var friendlyInstruct2Clock;
var instructMainTask_text_2;
var instructMainTask_keyResp_2;
var friendlyTaskClock;
var stimulus12;
var instructsurpA1_right_2;
var instructsurpA2_left_2;
var friendly_key_resp;
var finishMessageClock;
var finishMessage_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "JS_code"
  JS_codeClock = new util.Clock();
  // shuffle is push in JS so defining shuffle for our JS experiment code
  shuffle = util.shuffle;
  // Initialize components for Routine "setup"
  setupClock = new util.Clock();
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  welcome_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_text',
    text: 'Arrow Game\n\nWelcome to the arrow game. In this game, arrows will be quickly flashed on the screen. Your goal is to respond to the direction of the MIDDLE arrow, and to respond as quickly as you can without making mistakes. \n\nIf the MIDDLE arrow is pointing to the right, use your right hand to press the right button. If the MIDDLE arrow is pointing to the left, use your left hand to press the left button. \n\nPress the right button to continue\n',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  welcome_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructRight"
  instructRightClock = new util.Clock();
  instructRight_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructRight_text',
    text: 'Below, the MIDDLE arrow is pointing to the right, so you would respond by pressing the right button with your right hand.\n\nPress the right button to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instructRight_centerImg = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructRight_centerImg', units : undefined, 
    image : 'img/rightArrow.png', mask : undefined,
    ori : 0, pos : [0, (- 0.3)], size : [0.02, 0.02],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  instructRight_rightImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructRight_rightImg1', units : undefined, 
    image : 'img/rightArrow.png', mask : undefined,
    ori : 0, pos : [0.03, (- 0.3)], size : [0.02, 0.02],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  instructRight_leftImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructRight_leftImg1', units : undefined, 
    image : 'img/rightArrow.png', mask : undefined,
    ori : 0, pos : [(- 0.03), (- 0.3)], size : [0.02, 0.02],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -3.0 
  });
  insructRight_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructLeft"
  instructLeftClock = new util.Clock();
  instructLeft_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructLeft_text',
    text: 'Below, the MIDDLE arrow is pointing to the left, so you would respond by pressing the left button with your left hand.\n\nPress the left button to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instructLeft_centerImg = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructLeft_centerImg', units : undefined, 
    image : 'img/leftArrow.png', mask : undefined,
    ori : 0, pos : [0, (- 0.3)], size : [0.02, 0.02],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  instructLeft_rightImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructLeft_rightImg1', units : undefined, 
    image : 'img/leftArrow.png', mask : undefined,
    ori : 0, pos : [0.03, (- 0.3)], size : [0.02, 0.02],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  instructLeft_leftImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructLeft_leftImg1', units : undefined, 
    image : 'img/leftArrow.png', mask : undefined,
    ori : 0, pos : [(- 0.03), (- 0.3)], size : [0.02, 0.02],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -3.0 
  });
  instructLeft_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructInconRight"
  instructInconRightClock = new util.Clock();
  instructInconRight_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructInconRight_text',
    text: 'Sometimes the MIDDLE arrow will point in a different direction from the other arrows. However, your goal is to always respond based on the direction of the MIDDLE arrow.\n\nBelow, the MIDDLE arrow is pointing to the right, so you would respond by pressing the right button with your right hand.\n\nPress the right button to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instructIncon_centerImg = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructIncon_centerImg', units : undefined, 
    image : 'img/rightArrow.png', mask : undefined,
    ori : 0, pos : [0, (- 0.3)], size : [0.02, 0.02],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  instructIncon_rightImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructIncon_rightImg1', units : undefined, 
    image : 'img/leftArrow.png', mask : undefined,
    ori : 0, pos : [0.03, (- 0.3)], size : [0.02, 0.02],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  instructIncon_leftImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructIncon_leftImg1', units : undefined, 
    image : 'img/leftArrow.png', mask : undefined,
    ori : 0, pos : [(- 0.03), (- 0.3)], size : [0.02, 0.02],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -3.0 
  });
  insructInconRight_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructInconLeft"
  instructInconLeftClock = new util.Clock();
  instructInconLeft_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructInconLeft_text',
    text: 'Below, the MIDDLE arrow is pointing to the left, so you would respond by pressing the left button with your left hand.\n\nPress the left button to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instructInconLeft_centerImg = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructInconLeft_centerImg', units : undefined, 
    image : 'img/leftArrow.png', mask : undefined,
    ori : 0, pos : [0, (- 0.3)], size : [0.02, 0.02],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  instructInconLeft_rightImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructInconLeft_rightImg1', units : undefined, 
    image : 'img/rightArrow.png', mask : undefined,
    ori : 0, pos : [0.03, (- 0.3)], size : [0.02, 0.02],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  instructInconLeft_leftImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructInconLeft_leftImg1', units : undefined, 
    image : 'img/rightArrow.png', mask : undefined,
    ori : 0, pos : [(- 0.03), (- 0.3)], size : [0.02, 0.02],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -3.0 
  });
  instructInconLeft_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_blockReminders"
  prac_blockRemindersClock = new util.Clock();
  trialNum = 0;
  accuracy = 0;
  numCorr = 0;
  blockAcc = 0;
  
  prac_blockText = new visual.TextStim({
    win: psychoJS.window,
    name: 'prac_blockText',
    text: 'Practice',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.06,  wrapWidth: 1.3, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  prac_reminder_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'prac_reminder_text',
    text: 'You will now practice responding to the arrows. Remember to always respond to the direction of the MIDDLE arrow.\n\nRespond as quickly as you can without making mistakes.\n\nTo get ready, rest your right and left index fingers on the right and left buttons, then press the right button when you are ready to begin.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  prac_reminder_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "initFixation"
  initFixationClock = new util.Clock();
  initFixation_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'initFixation_img', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.015)], size : [0.26, 0.22],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "prac_stimRoutine"
  prac_stimRoutineClock = new util.Clock();
  thisISI = 0;
  
  bigFace = new visual.ImageStim({
    win : psychoJS.window,
    name : 'bigFace', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.0], size : [0.4267, 0.3],
    color : new util.Color([1,1,1]), opacity : 0.85,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  cover_background_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cover_background_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, (- 0.015)], size : [0.26, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  prac_centerImg = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_centerImg', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -3.0 
  });
  prac_rightImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_rightImg1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -4.0 
  });
  prac_rightImg2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_rightImg2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -5.0 
  });
  prac_leftImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_leftImg1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -6.0 
  });
  prac_leftImg2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_leftImg2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -7.0 
  });
  prac_fixImg = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_fixImg', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.015)], size : [0.26, 0.22],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -8.0 
  });
  prac_stim_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_blockFeed"
  prac_blockFeedClock = new util.Clock();
  prac_blockFeed_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'prac_blockFeed_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  prac_pressContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'prac_pressContinue',
    text: 'Press the right key',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: 1.3, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  prac_blockFeed_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "task_blockReminders"
  task_blockRemindersClock = new util.Clock();
  blockCounter = 0;
  
  task_blockText = new visual.TextStim({
    win: psychoJS.window,
    name: 'task_blockText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.06,  wrapWidth: 1.3, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  task_blockReminders_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'task_blockReminders_text',
    text: 'Remember to always respond to the direction of the MIDDLE arrow.\n\nRespond as quickly as you can without making mistakes.\n\nTo get ready, rest your right and left index fingers on the right and left buttons, then press the right button when you are ready to begin.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  task_blockReminders_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "task_stimRoutine"
  task_stimRoutineClock = new util.Clock();
  bigFace_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'bigFace_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.0], size : [0.4267, 0.3],
    color : new util.Color([1,1,1]), opacity : 0.85,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  cover_background = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cover_background', units : undefined, 
    image : 'img/cover_background.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.015)], size : [0.26, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  task_centerImg = new visual.ImageStim({
    win : psychoJS.window,
    name : 'task_centerImg', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -3.0 
  });
  task_rightImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'task_rightImg1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -4.0 
  });
  task_rightImg2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'task_rightImg2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -5.0 
  });
  task_leftImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'task_leftImg1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -6.0 
  });
  task_leftImg2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'task_leftImg2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -7.0 
  });
  task_fixImg = new visual.ImageStim({
    win : psychoJS.window,
    name : 'task_fixImg', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.015)], size : [0.26, 0.22],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -8.0 
  });
  task1_stim_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "task_blockFeed"
  task_blockFeedClock = new util.Clock();
  task_blockFeed_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'task_blockFeed_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.12,  wrapWidth: 1.8, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  task_blockFeed_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'task_blockFeed_text2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  task_blockFeed_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation1"
  fixation1Clock = new util.Clock();
  fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "errorNumbers_2"
  errorNumbers_2Clock = new util.Clock();
  errorNumbers_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'errorNumbers_text_2',
    text: 'How many errors do you think you made in this game?\n\nTo answer the question: \nPlease type your answer using the Keyboard. \n\nPress the "C" key to continue.\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.12], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  textbox_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_2',
    text: '',
    font: 'Open Sans',
    pos: [0, (- 0.3)], letterHeight: 0.05,
    size: [0.2, 0.2],  units: undefined, 
    color: [(- 1.0), (- 1.0), (- 1.0)], colorSpace: 'rgb',
    fillColor: [1.0, 1.0, 1.0], borderColor: [(- 1.0), (- 1.0), (- 1.0)],
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    editable: true,
    multiline: true,
    anchor: 'bottom-center',
    depth: -2.0 
  });
  
  errorN_key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "botherRate"
  botherRateClock = new util.Clock();
  botherRate_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'botherRate_text',
    text: 'How much did it bother you when you made an error during the arrow game? \n\nTo answer this question: \nPlease call the experimenter and let them know your answer on a scale from 0 (not at all) to 10 (very much). \n\nPlease type your answer using the Keyboard. \n\nPress the "C" key to continue.\n\n\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.12], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  textbox_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_3',
    text: '',
    font: 'Open Sans',
    pos: [0, (- 0.3)], letterHeight: 0.05,
    size: [0.2, 0.2],  units: undefined, 
    color: [(- 1.0), (- 1.0), (- 1.0)], colorSpace: 'rgb',
    fillColor: [1.0, 1.0, 1.0], borderColor: [(- 1.0), (- 1.0), (- 1.0)],
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    editable: true,
    multiline: true,
    anchor: 'bottom-center',
    depth: -2.0 
  });
  
  botherRate_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "askExperimenter"
  askExperimenterClock = new util.Clock();
  // Initialize components for Routine "surpriseInstruct"
  surpriseInstructClock = new util.Clock();
  instruct_surprise1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_surprise1',
    text: 'You will now begin a game in which you will be asked if the displayed face on the screen looks OLD or NEW to you.  \n\n\nFor example, if you think that you have seen a displayed face in the previous game, please select OLD as your response.\n\nPress right key to proceed.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  instruct_surp1_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructSurpriseTask2_2"
  instructSurpriseTask2_2Clock = new util.Clock();
  instructMainTask_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructMainTask_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instructMainTask_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "surpriseTask"
  surpriseTaskClock = new util.Clock();
  stimulus = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stimulus', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.2], size : [0.71116667, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  instructsurpA1_right = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructsurpA1_right',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  instructsurpA2_left = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructsurpA2_left',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.6), (- 0.03)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  surprise_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "friendlyInstruct1"
  friendlyInstruct1Clock = new util.Clock();
  instruct_surprise1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_surprise1_2',
    text: 'You will now begin a game in which you will be asked if the displayed face on the screen looks friendly or unfriendly to you.  \n\n\nFor example, if you think that the displayed face looks friendly to you, please select Friendly as your response.\n\nPress right key to proceed.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  instruct_surp1_key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "friendlyInstruct2"
  friendlyInstruct2Clock = new util.Clock();
  instructMainTask_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructMainTask_text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instructMainTask_keyResp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "friendlyTask"
  friendlyTaskClock = new util.Clock();
  stimulus12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stimulus12', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.2], size : [0.71116667, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  instructsurpA1_right_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructsurpA1_right_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  instructsurpA2_left_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructsurpA2_left_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.6), (- 0.03)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  friendly_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "finishMessage"
  finishMessageClock = new util.Clock();
  finishMessage_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'finishMessage_text',
    text: 'Thank you for your participation!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var JS_codeComponents;
function JS_codeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'JS_code'-------
    t = 0;
    JS_codeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    JS_codeComponents = [];
    
    JS_codeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function JS_codeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'JS_code'-------
    // get current time
    t = JS_codeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    JS_codeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function JS_codeRoutineEnd() {
  return async function () {
    //------Ending Routine 'JS_code'-------
    JS_codeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "JS_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var setupComponents;
function setupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'setup'-------
    t = 0;
    setupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    setupComponents = [];
    
    setupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function setupRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'setup'-------
    // get current time
    t = setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    setupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function setupRoutineEnd() {
  return async function () {
    //------Ending Routine 'setup'-------
    setupComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _welcome_keyResp_allKeys;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'welcome'-------
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    welcome_keyResp.keys = undefined;
    welcome_keyResp.rt = undefined;
    _welcome_keyResp_allKeys = [];
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(welcome_text);
    welcomeComponents.push(welcome_keyResp);
    
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'welcome'-------
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome_text* updates
    if (t >= 0.0 && welcome_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_text.tStart = t;  // (not accounting for frame time here)
      welcome_text.frameNStart = frameN;  // exact frame index
      
      welcome_text.setAutoDraw(true);
    }

    
    // *welcome_keyResp* updates
    if (t >= 0.0 && welcome_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_keyResp.tStart = t;  // (not accounting for frame time here)
      welcome_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcome_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcome_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcome_keyResp.clearEvents(); });
    }

    if (welcome_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcome_keyResp.getKeys({keyList: ['right'], waitRelease: false});
      _welcome_keyResp_allKeys = _welcome_keyResp_allKeys.concat(theseKeys);
      if (_welcome_keyResp_allKeys.length > 0) {
        welcome_keyResp.keys = _welcome_keyResp_allKeys[_welcome_keyResp_allKeys.length - 1].name;  // just the last key pressed
        welcome_keyResp.rt = _welcome_keyResp_allKeys[_welcome_keyResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd() {
  return async function () {
    //------Ending Routine 'welcome'-------
    welcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    welcome_keyResp.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _insructRight_keyResp_allKeys;
var instructRightComponents;
function instructRightRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instructRight'-------
    t = 0;
    instructRightClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    insructRight_keyResp.keys = undefined;
    insructRight_keyResp.rt = undefined;
    _insructRight_keyResp_allKeys = [];
    // keep track of which components have finished
    instructRightComponents = [];
    instructRightComponents.push(instructRight_text);
    instructRightComponents.push(instructRight_centerImg);
    instructRightComponents.push(instructRight_rightImg1);
    instructRightComponents.push(instructRight_leftImg1);
    instructRightComponents.push(insructRight_keyResp);
    
    instructRightComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructRightRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instructRight'-------
    // get current time
    t = instructRightClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructRight_text* updates
    if (t >= 0.0 && instructRight_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructRight_text.tStart = t;  // (not accounting for frame time here)
      instructRight_text.frameNStart = frameN;  // exact frame index
      
      instructRight_text.setAutoDraw(true);
    }

    
    // *instructRight_centerImg* updates
    if (t >= 0.0 && instructRight_centerImg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructRight_centerImg.tStart = t;  // (not accounting for frame time here)
      instructRight_centerImg.frameNStart = frameN;  // exact frame index
      
      instructRight_centerImg.setAutoDraw(true);
    }

    
    // *instructRight_rightImg1* updates
    if (t >= 0.0 && instructRight_rightImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructRight_rightImg1.tStart = t;  // (not accounting for frame time here)
      instructRight_rightImg1.frameNStart = frameN;  // exact frame index
      
      instructRight_rightImg1.setAutoDraw(true);
    }

    
    // *instructRight_leftImg1* updates
    if (t >= 0.0 && instructRight_leftImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructRight_leftImg1.tStart = t;  // (not accounting for frame time here)
      instructRight_leftImg1.frameNStart = frameN;  // exact frame index
      
      instructRight_leftImg1.setAutoDraw(true);
    }

    
    // *insructRight_keyResp* updates
    if (t >= 0.0 && insructRight_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      insructRight_keyResp.tStart = t;  // (not accounting for frame time here)
      insructRight_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { insructRight_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { insructRight_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { insructRight_keyResp.clearEvents(); });
    }

    if (insructRight_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = insructRight_keyResp.getKeys({keyList: ['right'], waitRelease: false});
      _insructRight_keyResp_allKeys = _insructRight_keyResp_allKeys.concat(theseKeys);
      if (_insructRight_keyResp_allKeys.length > 0) {
        insructRight_keyResp.keys = _insructRight_keyResp_allKeys[_insructRight_keyResp_allKeys.length - 1].name;  // just the last key pressed
        insructRight_keyResp.rt = _insructRight_keyResp_allKeys[_insructRight_keyResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructRightComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructRightRoutineEnd() {
  return async function () {
    //------Ending Routine 'instructRight'-------
    instructRightComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    insructRight_keyResp.stop();
    // the Routine "instructRight" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _instructLeft_keyResp_allKeys;
var instructLeftComponents;
function instructLeftRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instructLeft'-------
    t = 0;
    instructLeftClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instructLeft_keyResp.keys = undefined;
    instructLeft_keyResp.rt = undefined;
    _instructLeft_keyResp_allKeys = [];
    // keep track of which components have finished
    instructLeftComponents = [];
    instructLeftComponents.push(instructLeft_text);
    instructLeftComponents.push(instructLeft_centerImg);
    instructLeftComponents.push(instructLeft_rightImg1);
    instructLeftComponents.push(instructLeft_leftImg1);
    instructLeftComponents.push(instructLeft_keyResp);
    
    instructLeftComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructLeftRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instructLeft'-------
    // get current time
    t = instructLeftClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructLeft_text* updates
    if (t >= 0.0 && instructLeft_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructLeft_text.tStart = t;  // (not accounting for frame time here)
      instructLeft_text.frameNStart = frameN;  // exact frame index
      
      instructLeft_text.setAutoDraw(true);
    }

    
    // *instructLeft_centerImg* updates
    if (t >= 0.0 && instructLeft_centerImg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructLeft_centerImg.tStart = t;  // (not accounting for frame time here)
      instructLeft_centerImg.frameNStart = frameN;  // exact frame index
      
      instructLeft_centerImg.setAutoDraw(true);
    }

    
    // *instructLeft_rightImg1* updates
    if (t >= 0.0 && instructLeft_rightImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructLeft_rightImg1.tStart = t;  // (not accounting for frame time here)
      instructLeft_rightImg1.frameNStart = frameN;  // exact frame index
      
      instructLeft_rightImg1.setAutoDraw(true);
    }

    
    // *instructLeft_leftImg1* updates
    if (t >= 0.0 && instructLeft_leftImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructLeft_leftImg1.tStart = t;  // (not accounting for frame time here)
      instructLeft_leftImg1.frameNStart = frameN;  // exact frame index
      
      instructLeft_leftImg1.setAutoDraw(true);
    }

    
    // *instructLeft_keyResp* updates
    if (t >= 0.0 && instructLeft_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructLeft_keyResp.tStart = t;  // (not accounting for frame time here)
      instructLeft_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructLeft_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructLeft_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructLeft_keyResp.clearEvents(); });
    }

    if (instructLeft_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructLeft_keyResp.getKeys({keyList: ['left'], waitRelease: false});
      _instructLeft_keyResp_allKeys = _instructLeft_keyResp_allKeys.concat(theseKeys);
      if (_instructLeft_keyResp_allKeys.length > 0) {
        instructLeft_keyResp.keys = _instructLeft_keyResp_allKeys[_instructLeft_keyResp_allKeys.length - 1].name;  // just the last key pressed
        instructLeft_keyResp.rt = _instructLeft_keyResp_allKeys[_instructLeft_keyResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructLeftComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructLeftRoutineEnd() {
  return async function () {
    //------Ending Routine 'instructLeft'-------
    instructLeftComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    instructLeft_keyResp.stop();
    // the Routine "instructLeft" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _insructInconRight_keyResp_allKeys;
var instructInconRightComponents;
function instructInconRightRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instructInconRight'-------
    t = 0;
    instructInconRightClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    insructInconRight_keyResp.keys = undefined;
    insructInconRight_keyResp.rt = undefined;
    _insructInconRight_keyResp_allKeys = [];
    // keep track of which components have finished
    instructInconRightComponents = [];
    instructInconRightComponents.push(instructInconRight_text);
    instructInconRightComponents.push(instructIncon_centerImg);
    instructInconRightComponents.push(instructIncon_rightImg1);
    instructInconRightComponents.push(instructIncon_leftImg1);
    instructInconRightComponents.push(insructInconRight_keyResp);
    
    instructInconRightComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructInconRightRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instructInconRight'-------
    // get current time
    t = instructInconRightClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructInconRight_text* updates
    if (t >= 0.0 && instructInconRight_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructInconRight_text.tStart = t;  // (not accounting for frame time here)
      instructInconRight_text.frameNStart = frameN;  // exact frame index
      
      instructInconRight_text.setAutoDraw(true);
    }

    
    // *instructIncon_centerImg* updates
    if (t >= 0.0 && instructIncon_centerImg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructIncon_centerImg.tStart = t;  // (not accounting for frame time here)
      instructIncon_centerImg.frameNStart = frameN;  // exact frame index
      
      instructIncon_centerImg.setAutoDraw(true);
    }

    
    // *instructIncon_rightImg1* updates
    if (t >= 0.0 && instructIncon_rightImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructIncon_rightImg1.tStart = t;  // (not accounting for frame time here)
      instructIncon_rightImg1.frameNStart = frameN;  // exact frame index
      
      instructIncon_rightImg1.setAutoDraw(true);
    }

    
    // *instructIncon_leftImg1* updates
    if (t >= 0.0 && instructIncon_leftImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructIncon_leftImg1.tStart = t;  // (not accounting for frame time here)
      instructIncon_leftImg1.frameNStart = frameN;  // exact frame index
      
      instructIncon_leftImg1.setAutoDraw(true);
    }

    
    // *insructInconRight_keyResp* updates
    if (t >= 0.0 && insructInconRight_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      insructInconRight_keyResp.tStart = t;  // (not accounting for frame time here)
      insructInconRight_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { insructInconRight_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { insructInconRight_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { insructInconRight_keyResp.clearEvents(); });
    }

    if (insructInconRight_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = insructInconRight_keyResp.getKeys({keyList: ['right'], waitRelease: false});
      _insructInconRight_keyResp_allKeys = _insructInconRight_keyResp_allKeys.concat(theseKeys);
      if (_insructInconRight_keyResp_allKeys.length > 0) {
        insructInconRight_keyResp.keys = _insructInconRight_keyResp_allKeys[_insructInconRight_keyResp_allKeys.length - 1].name;  // just the last key pressed
        insructInconRight_keyResp.rt = _insructInconRight_keyResp_allKeys[_insructInconRight_keyResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructInconRightComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructInconRightRoutineEnd() {
  return async function () {
    //------Ending Routine 'instructInconRight'-------
    instructInconRightComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    insructInconRight_keyResp.stop();
    // the Routine "instructInconRight" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _instructInconLeft_keyResp_allKeys;
var instructInconLeftComponents;
function instructInconLeftRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instructInconLeft'-------
    t = 0;
    instructInconLeftClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instructInconLeft_keyResp.keys = undefined;
    instructInconLeft_keyResp.rt = undefined;
    _instructInconLeft_keyResp_allKeys = [];
    // keep track of which components have finished
    instructInconLeftComponents = [];
    instructInconLeftComponents.push(instructInconLeft_text);
    instructInconLeftComponents.push(instructInconLeft_centerImg);
    instructInconLeftComponents.push(instructInconLeft_rightImg1);
    instructInconLeftComponents.push(instructInconLeft_leftImg1);
    instructInconLeftComponents.push(instructInconLeft_keyResp);
    
    instructInconLeftComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructInconLeftRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instructInconLeft'-------
    // get current time
    t = instructInconLeftClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructInconLeft_text* updates
    if (t >= 0.0 && instructInconLeft_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructInconLeft_text.tStart = t;  // (not accounting for frame time here)
      instructInconLeft_text.frameNStart = frameN;  // exact frame index
      
      instructInconLeft_text.setAutoDraw(true);
    }

    
    // *instructInconLeft_centerImg* updates
    if (t >= 0.0 && instructInconLeft_centerImg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructInconLeft_centerImg.tStart = t;  // (not accounting for frame time here)
      instructInconLeft_centerImg.frameNStart = frameN;  // exact frame index
      
      instructInconLeft_centerImg.setAutoDraw(true);
    }

    
    // *instructInconLeft_rightImg1* updates
    if (t >= 0.0 && instructInconLeft_rightImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructInconLeft_rightImg1.tStart = t;  // (not accounting for frame time here)
      instructInconLeft_rightImg1.frameNStart = frameN;  // exact frame index
      
      instructInconLeft_rightImg1.setAutoDraw(true);
    }

    
    // *instructInconLeft_leftImg1* updates
    if (t >= 0.0 && instructInconLeft_leftImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructInconLeft_leftImg1.tStart = t;  // (not accounting for frame time here)
      instructInconLeft_leftImg1.frameNStart = frameN;  // exact frame index
      
      instructInconLeft_leftImg1.setAutoDraw(true);
    }

    
    // *instructInconLeft_keyResp* updates
    if (t >= 0.0 && instructInconLeft_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructInconLeft_keyResp.tStart = t;  // (not accounting for frame time here)
      instructInconLeft_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructInconLeft_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructInconLeft_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructInconLeft_keyResp.clearEvents(); });
    }

    if (instructInconLeft_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructInconLeft_keyResp.getKeys({keyList: ['left'], waitRelease: false});
      _instructInconLeft_keyResp_allKeys = _instructInconLeft_keyResp_allKeys.concat(theseKeys);
      if (_instructInconLeft_keyResp_allKeys.length > 0) {
        instructInconLeft_keyResp.keys = _instructInconLeft_keyResp_allKeys[_instructInconLeft_keyResp_allKeys.length - 1].name;  // just the last key pressed
        instructInconLeft_keyResp.rt = _instructInconLeft_keyResp_allKeys[_instructInconLeft_keyResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructInconLeftComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructInconLeftRoutineEnd() {
  return async function () {
    //------Ending Routine 'instructInconLeft'-------
    instructInconLeftComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    instructInconLeft_keyResp.stop();
    // the Routine "instructInconLeft" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var prac_block_loop;
var currentLoop;
function prac_block_loopLoopBegin(prac_block_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_block_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 999, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'blockSelect_practice.csv',
      seed: undefined, name: 'prac_block_loop'
    });
    psychoJS.experiment.addLoop(prac_block_loop); // add the loop to the experiment
    currentLoop = prac_block_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    prac_block_loop.forEach(function() {
      const snapshot = prac_block_loop.getSnapshot();
    
      prac_block_loopLoopScheduler.add(importConditions(snapshot));
      prac_block_loopLoopScheduler.add(prac_blockRemindersRoutineBegin(snapshot));
      prac_block_loopLoopScheduler.add(prac_blockRemindersRoutineEachFrame());
      prac_block_loopLoopScheduler.add(prac_blockRemindersRoutineEnd());
      prac_block_loopLoopScheduler.add(initFixationRoutineBegin(snapshot));
      prac_block_loopLoopScheduler.add(initFixationRoutineEachFrame());
      prac_block_loopLoopScheduler.add(initFixationRoutineEnd());
      const prac_trial_loopLoopScheduler = new Scheduler(psychoJS);
      prac_block_loopLoopScheduler.add(prac_trial_loopLoopBegin(prac_trial_loopLoopScheduler, snapshot));
      prac_block_loopLoopScheduler.add(prac_trial_loopLoopScheduler);
      prac_block_loopLoopScheduler.add(prac_trial_loopLoopEnd);
      prac_block_loopLoopScheduler.add(prac_blockFeedRoutineBegin(snapshot));
      prac_block_loopLoopScheduler.add(prac_blockFeedRoutineEachFrame());
      prac_block_loopLoopScheduler.add(prac_blockFeedRoutineEnd());
      prac_block_loopLoopScheduler.add(endLoopIteration(prac_block_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var prac_trial_loop;
function prac_trial_loopLoopBegin(prac_trial_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_trial_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: whichBlock,
      seed: undefined, name: 'prac_trial_loop'
    });
    psychoJS.experiment.addLoop(prac_trial_loop); // add the loop to the experiment
    currentLoop = prac_trial_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    prac_trial_loop.forEach(function() {
      const snapshot = prac_trial_loop.getSnapshot();
    
      prac_trial_loopLoopScheduler.add(importConditions(snapshot));
      prac_trial_loopLoopScheduler.add(prac_stimRoutineRoutineBegin(snapshot));
      prac_trial_loopLoopScheduler.add(prac_stimRoutineRoutineEachFrame());
      prac_trial_loopLoopScheduler.add(prac_stimRoutineRoutineEnd());
      prac_trial_loopLoopScheduler.add(endLoopIteration(prac_trial_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function prac_trial_loopLoopEnd() {
  psychoJS.experiment.removeLoop(prac_trial_loop);

  return Scheduler.Event.NEXT;
}


async function prac_block_loopLoopEnd() {
  psychoJS.experiment.removeLoop(prac_block_loop);

  return Scheduler.Event.NEXT;
}


var task_block_loop;
function task_block_loopLoopBegin(task_block_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    task_block_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'blockSelect.csv',
      seed: undefined, name: 'task_block_loop'
    });
    psychoJS.experiment.addLoop(task_block_loop); // add the loop to the experiment
    currentLoop = task_block_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    task_block_loop.forEach(function() {
      const snapshot = task_block_loop.getSnapshot();
    
      task_block_loopLoopScheduler.add(importConditions(snapshot));
      task_block_loopLoopScheduler.add(task_blockRemindersRoutineBegin(snapshot));
      task_block_loopLoopScheduler.add(task_blockRemindersRoutineEachFrame());
      task_block_loopLoopScheduler.add(task_blockRemindersRoutineEnd());
      task_block_loopLoopScheduler.add(initFixationRoutineBegin(snapshot));
      task_block_loopLoopScheduler.add(initFixationRoutineEachFrame());
      task_block_loopLoopScheduler.add(initFixationRoutineEnd());
      const task_trial_loopLoopScheduler = new Scheduler(psychoJS);
      task_block_loopLoopScheduler.add(task_trial_loopLoopBegin(task_trial_loopLoopScheduler, snapshot));
      task_block_loopLoopScheduler.add(task_trial_loopLoopScheduler);
      task_block_loopLoopScheduler.add(task_trial_loopLoopEnd);
      task_block_loopLoopScheduler.add(task_blockFeedRoutineBegin(snapshot));
      task_block_loopLoopScheduler.add(task_blockFeedRoutineEachFrame());
      task_block_loopLoopScheduler.add(task_blockFeedRoutineEnd());
      task_block_loopLoopScheduler.add(endLoopIteration(task_block_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var task_trial_loop;
function task_trial_loopLoopBegin(task_trial_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    task_trial_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: whichBlock,
      seed: undefined, name: 'task_trial_loop'
    });
    psychoJS.experiment.addLoop(task_trial_loop); // add the loop to the experiment
    currentLoop = task_trial_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    task_trial_loop.forEach(function() {
      const snapshot = task_trial_loop.getSnapshot();
    
      task_trial_loopLoopScheduler.add(importConditions(snapshot));
      task_trial_loopLoopScheduler.add(task_stimRoutineRoutineBegin(snapshot));
      task_trial_loopLoopScheduler.add(task_stimRoutineRoutineEachFrame());
      task_trial_loopLoopScheduler.add(task_stimRoutineRoutineEnd());
      task_trial_loopLoopScheduler.add(endLoopIteration(task_trial_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function task_trial_loopLoopEnd() {
  psychoJS.experiment.removeLoop(task_trial_loop);

  return Scheduler.Event.NEXT;
}


async function task_block_loopLoopEnd() {
  psychoJS.experiment.removeLoop(task_block_loop);

  return Scheduler.Event.NEXT;
}


var surprise_block_loop;
function surprise_block_loopLoopBegin(surprise_block_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    surprise_block_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: (("surpriseBlock_select_" + expInfo["cb"]) + ".xlsx"),
      seed: undefined, name: 'surprise_block_loop'
    });
    psychoJS.experiment.addLoop(surprise_block_loop); // add the loop to the experiment
    currentLoop = surprise_block_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    surprise_block_loop.forEach(function() {
      const snapshot = surprise_block_loop.getSnapshot();
    
      surprise_block_loopLoopScheduler.add(importConditions(snapshot));
      surprise_block_loopLoopScheduler.add(instructSurpriseTask2_2RoutineBegin(snapshot));
      surprise_block_loopLoopScheduler.add(instructSurpriseTask2_2RoutineEachFrame());
      surprise_block_loopLoopScheduler.add(instructSurpriseTask2_2RoutineEnd());
      const trialsLoopScheduler = new Scheduler(psychoJS);
      surprise_block_loopLoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      surprise_block_loopLoopScheduler.add(trialsLoopScheduler);
      surprise_block_loopLoopScheduler.add(trialsLoopEnd);
      surprise_block_loopLoopScheduler.add(endLoopIteration(surprise_block_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: whichSurpriseBlock,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      const snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(surpriseTaskRoutineBegin(snapshot));
      trialsLoopScheduler.add(surpriseTaskRoutineEachFrame());
      trialsLoopScheduler.add(surpriseTaskRoutineEnd());
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


async function surprise_block_loopLoopEnd() {
  psychoJS.experiment.removeLoop(surprise_block_loop);

  return Scheduler.Event.NEXT;
}


var friendly_block_loop;
function friendly_block_loopLoopBegin(friendly_block_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    friendly_block_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: (("friendlyBlock_select_" + expInfo["friendly"]) + ".xlsx"),
      seed: undefined, name: 'friendly_block_loop'
    });
    psychoJS.experiment.addLoop(friendly_block_loop); // add the loop to the experiment
    currentLoop = friendly_block_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    friendly_block_loop.forEach(function() {
      const snapshot = friendly_block_loop.getSnapshot();
    
      friendly_block_loopLoopScheduler.add(importConditions(snapshot));
      friendly_block_loopLoopScheduler.add(friendlyInstruct2RoutineBegin(snapshot));
      friendly_block_loopLoopScheduler.add(friendlyInstruct2RoutineEachFrame());
      friendly_block_loopLoopScheduler.add(friendlyInstruct2RoutineEnd());
      const trials_2LoopScheduler = new Scheduler(psychoJS);
      friendly_block_loopLoopScheduler.add(trials_2LoopBegin(trials_2LoopScheduler, snapshot));
      friendly_block_loopLoopScheduler.add(trials_2LoopScheduler);
      friendly_block_loopLoopScheduler.add(trials_2LoopEnd);
      friendly_block_loopLoopScheduler.add(endLoopIteration(friendly_block_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: whichSurpriseBlock,
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      const snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(friendlyTaskRoutineBegin(snapshot));
      trials_2LoopScheduler.add(friendlyTaskRoutineEachFrame());
      trials_2LoopScheduler.add(friendlyTaskRoutineEnd());
      trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


async function friendly_block_loopLoopEnd() {
  psychoJS.experiment.removeLoop(friendly_block_loop);

  return Scheduler.Event.NEXT;
}


var _prac_reminder_keyResp_allKeys;
var prac_blockRemindersComponents;
function prac_blockRemindersRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'prac_blockReminders'-------
    t = 0;
    prac_blockRemindersClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    prac_reminder_keyResp.keys = undefined;
    prac_reminder_keyResp.rt = undefined;
    _prac_reminder_keyResp_allKeys = [];
    // keep track of which components have finished
    prac_blockRemindersComponents = [];
    prac_blockRemindersComponents.push(prac_blockText);
    prac_blockRemindersComponents.push(prac_reminder_text);
    prac_blockRemindersComponents.push(prac_reminder_keyResp);
    
    prac_blockRemindersComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_blockRemindersRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'prac_blockReminders'-------
    // get current time
    t = prac_blockRemindersClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_blockText* updates
    if (t >= 0.0 && prac_blockText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_blockText.tStart = t;  // (not accounting for frame time here)
      prac_blockText.frameNStart = frameN;  // exact frame index
      
      prac_blockText.setAutoDraw(true);
    }

    
    // *prac_reminder_text* updates
    if (t >= 0.0 && prac_reminder_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_reminder_text.tStart = t;  // (not accounting for frame time here)
      prac_reminder_text.frameNStart = frameN;  // exact frame index
      
      prac_reminder_text.setAutoDraw(true);
    }

    
    // *prac_reminder_keyResp* updates
    if (t >= 0.0 && prac_reminder_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_reminder_keyResp.tStart = t;  // (not accounting for frame time here)
      prac_reminder_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_reminder_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_reminder_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prac_reminder_keyResp.clearEvents(); });
    }

    if (prac_reminder_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_reminder_keyResp.getKeys({keyList: ['right'], waitRelease: false});
      _prac_reminder_keyResp_allKeys = _prac_reminder_keyResp_allKeys.concat(theseKeys);
      if (_prac_reminder_keyResp_allKeys.length > 0) {
        prac_reminder_keyResp.keys = _prac_reminder_keyResp_allKeys[_prac_reminder_keyResp_allKeys.length - 1].name;  // just the last key pressed
        prac_reminder_keyResp.rt = _prac_reminder_keyResp_allKeys[_prac_reminder_keyResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_blockRemindersComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_blockRemindersRoutineEnd() {
  return async function () {
    //------Ending Routine 'prac_blockReminders'-------
    prac_blockRemindersComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(prac_reminder_keyResp.corr, level);
    }
    psychoJS.experiment.addData('prac_reminder_keyResp.keys', prac_reminder_keyResp.keys);
    if (typeof prac_reminder_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_reminder_keyResp.rt', prac_reminder_keyResp.rt);
        routineTimer.reset();
        }
    
    prac_reminder_keyResp.stop();
    // the Routine "prac_blockReminders" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var initFixationComponents;
function initFixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'initFixation'-------
    t = 0;
    initFixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    initFixation_img.setImage('img/transp_fixation.png');
    // keep track of which components have finished
    initFixationComponents = [];
    initFixationComponents.push(initFixation_img);
    
    initFixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function initFixationRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'initFixation'-------
    // get current time
    t = initFixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *initFixation_img* updates
    if (t >= 0.0 && initFixation_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      initFixation_img.tStart = t;  // (not accounting for frame time here)
      initFixation_img.frameNStart = frameN;  // exact frame index
      
      initFixation_img.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (initFixation_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      initFixation_img.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    initFixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function initFixationRoutineEnd() {
  return async function () {
    //------Ending Routine 'initFixation'-------
    initFixationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var ISIRange;
var _prac_stim_keyResp_allKeys;
var prac_stimRoutineComponents;
function prac_stimRoutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'prac_stimRoutine'-------
    t = 0;
    prac_stimRoutineClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ISIRange = np.linspace(3500, 4000, 500);
    util.shuffle(ISIRange);
    thisISI = (ISIRange[0] / 1000);
    prac_trial_loop.addData("ISI", thisISI);
    
    bigFace.setImage(straightFace);
    cover_background_2.setImage('img/cover_background.png');
    prac_centerImg.setPos(locationC);
    prac_centerImg.setSize(imageSize);
    prac_centerImg.setImage(middleStim);
    prac_rightImg1.setPos(locationR);
    prac_rightImg1.setSize(imageSize);
    prac_rightImg1.setImage(rightStim);
    prac_rightImg2.setPos([0.077, 0]);
    prac_rightImg2.setSize(imageSize);
    prac_rightImg2.setImage(rightStim);
    prac_leftImg1.setPos(locationL);
    prac_leftImg1.setSize(imageSize);
    prac_leftImg1.setImage(leftStim);
    prac_leftImg2.setPos([(- 0.077), 0]);
    prac_leftImg2.setSize(imageSize);
    prac_leftImg2.setImage(leftStim);
    prac_fixImg.setImage('img/transp_fixation.png');
    prac_stim_keyResp.keys = undefined;
    prac_stim_keyResp.rt = undefined;
    _prac_stim_keyResp_allKeys = [];
    // keep track of which components have finished
    prac_stimRoutineComponents = [];
    prac_stimRoutineComponents.push(bigFace);
    prac_stimRoutineComponents.push(cover_background_2);
    prac_stimRoutineComponents.push(prac_centerImg);
    prac_stimRoutineComponents.push(prac_rightImg1);
    prac_stimRoutineComponents.push(prac_rightImg2);
    prac_stimRoutineComponents.push(prac_leftImg1);
    prac_stimRoutineComponents.push(prac_leftImg2);
    prac_stimRoutineComponents.push(prac_fixImg);
    prac_stimRoutineComponents.push(prac_stim_keyResp);
    
    prac_stimRoutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_stimRoutineRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'prac_stimRoutine'-------
    // get current time
    t = prac_stimRoutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *bigFace* updates
    if (t >= 0.0 && bigFace.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bigFace.tStart = t;  // (not accounting for frame time here)
      bigFace.frameNStart = frameN;  // exact frame index
      
      bigFace.setAutoDraw(true);
    }

    frameRemains = 0.0 + thisISI - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (bigFace.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      bigFace.setAutoDraw(false);
    }
    
    // *cover_background_2* updates
    if (t >= 0.0 && cover_background_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cover_background_2.tStart = t;  // (not accounting for frame time here)
      cover_background_2.frameNStart = frameN;  // exact frame index
      
      cover_background_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.35 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cover_background_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cover_background_2.setAutoDraw(false);
    }
    
    // *prac_centerImg* updates
    if (t >= 0.15 && prac_centerImg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_centerImg.tStart = t;  // (not accounting for frame time here)
      prac_centerImg.frameNStart = frameN;  // exact frame index
      
      prac_centerImg.setAutoDraw(true);
    }

    frameRemains = 0.15 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_centerImg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_centerImg.setAutoDraw(false);
    }
    
    // *prac_rightImg1* updates
    if (t >= 0.0 && prac_rightImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_rightImg1.tStart = t;  // (not accounting for frame time here)
      prac_rightImg1.frameNStart = frameN;  // exact frame index
      
      prac_rightImg1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.35 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_rightImg1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_rightImg1.setAutoDraw(false);
    }
    
    // *prac_rightImg2* updates
    if (t >= 0.0 && prac_rightImg2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_rightImg2.tStart = t;  // (not accounting for frame time here)
      prac_rightImg2.frameNStart = frameN;  // exact frame index
      
      prac_rightImg2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.35 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_rightImg2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_rightImg2.setAutoDraw(false);
    }
    
    // *prac_leftImg1* updates
    if (t >= 0.0 && prac_leftImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_leftImg1.tStart = t;  // (not accounting for frame time here)
      prac_leftImg1.frameNStart = frameN;  // exact frame index
      
      prac_leftImg1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.35 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_leftImg1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_leftImg1.setAutoDraw(false);
    }
    
    // *prac_leftImg2* updates
    if (t >= 0.0 && prac_leftImg2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_leftImg2.tStart = t;  // (not accounting for frame time here)
      prac_leftImg2.frameNStart = frameN;  // exact frame index
      
      prac_leftImg2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.35 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_leftImg2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_leftImg2.setAutoDraw(false);
    }
    
    // *prac_fixImg* updates
    if (t >= 0.0 && prac_fixImg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_fixImg.tStart = t;  // (not accounting for frame time here)
      prac_fixImg.frameNStart = frameN;  // exact frame index
      
      prac_fixImg.setAutoDraw(true);
    }

    frameRemains = 0.0 + thisISI - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_fixImg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_fixImg.setAutoDraw(false);
    }
    
    // *prac_stim_keyResp* updates
    if (t >= 0.0 && prac_stim_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_stim_keyResp.tStart = t;  // (not accounting for frame time here)
      prac_stim_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_stim_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_stim_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prac_stim_keyResp.clearEvents(); });
    }

    frameRemains = 0.0 + thisISI - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_stim_keyResp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_stim_keyResp.status = PsychoJS.Status.FINISHED;
  }

    if (prac_stim_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_stim_keyResp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _prac_stim_keyResp_allKeys = _prac_stim_keyResp_allKeys.concat(theseKeys);
      if (_prac_stim_keyResp_allKeys.length > 0) {
        prac_stim_keyResp.keys = _prac_stim_keyResp_allKeys.map((key) => key.name);  // storing all keys
        prac_stim_keyResp.rt = _prac_stim_keyResp_allKeys.map((key) => key.rt);
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_stimRoutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_stimRoutineRoutineEnd() {
  return async function () {
    //------Ending Routine 'prac_stimRoutine'-------
    prac_stimRoutineComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(prac_stim_keyResp.corr, level);
    }
    psychoJS.experiment.addData('prac_stim_keyResp.keys', prac_stim_keyResp.keys);
    if (typeof prac_stim_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_stim_keyResp.rt', prac_stim_keyResp.rt);
        }
    
    prac_stim_keyResp.stop();
    trialNum = (trialNum + 1);
    if (prac_stim_keyResp.keys) {
        if ((prac_stim_keyResp.keys[0] === "left")) {
            if ((target === "left")) {
                accuracy = 1;
                numCorr = (numCorr + 1);
            } else {
                if ((target === "right")) {
                    accuracy = 0;
                }
            }
        } else {
            if ((prac_stim_keyResp.keys[0] === "right")) {
                if ((target === "right")) {
                    accuracy = 1;
                    numCorr = (numCorr + 1);
                } else {
                    if ((target === "left")) {
                        accuracy = 0;
                    }
                }
            }
        }
    }
    prac_trial_loop.addData("accuracy", accuracy);
    
    // the Routine "prac_stimRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var outPut;
var _prac_blockFeed_keyResp_allKeys;
var prac_blockFeedComponents;
function prac_blockFeedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'prac_blockFeed'-------
    t = 0;
    prac_blockFeedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    blockAcc = (numCorr / trialNum);
    if ((blockAcc >= 0.75)) {
        outPut = "You have completed the practice";
        prac_block_loop.finished = true;
    } else {
        if ((blockAcc <= 0.75)) {
            outPut = "Please try the practice again";
            prac_block_loop.finished = false;
        }
    }
    trialNum = 0;
    numCorr = 0;
    
    prac_blockFeed_text.setText(outPut);
    prac_blockFeed_keyResp.keys = undefined;
    prac_blockFeed_keyResp.rt = undefined;
    _prac_blockFeed_keyResp_allKeys = [];
    // keep track of which components have finished
    prac_blockFeedComponents = [];
    prac_blockFeedComponents.push(prac_blockFeed_text);
    prac_blockFeedComponents.push(prac_pressContinue);
    prac_blockFeedComponents.push(prac_blockFeed_keyResp);
    
    prac_blockFeedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_blockFeedRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'prac_blockFeed'-------
    // get current time
    t = prac_blockFeedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_blockFeed_text* updates
    if (t >= 0.0 && prac_blockFeed_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_blockFeed_text.tStart = t;  // (not accounting for frame time here)
      prac_blockFeed_text.frameNStart = frameN;  // exact frame index
      
      prac_blockFeed_text.setAutoDraw(true);
    }

    
    // *prac_pressContinue* updates
    if (t >= 0.0 && prac_pressContinue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_pressContinue.tStart = t;  // (not accounting for frame time here)
      prac_pressContinue.frameNStart = frameN;  // exact frame index
      
      prac_pressContinue.setAutoDraw(true);
    }

    
    // *prac_blockFeed_keyResp* updates
    if (t >= 0.0 && prac_blockFeed_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_blockFeed_keyResp.tStart = t;  // (not accounting for frame time here)
      prac_blockFeed_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_blockFeed_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_blockFeed_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prac_blockFeed_keyResp.clearEvents(); });
    }

    if (prac_blockFeed_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_blockFeed_keyResp.getKeys({keyList: ['right'], waitRelease: false});
      _prac_blockFeed_keyResp_allKeys = _prac_blockFeed_keyResp_allKeys.concat(theseKeys);
      if (_prac_blockFeed_keyResp_allKeys.length > 0) {
        prac_blockFeed_keyResp.keys = _prac_blockFeed_keyResp_allKeys[_prac_blockFeed_keyResp_allKeys.length - 1].name;  // just the last key pressed
        prac_blockFeed_keyResp.rt = _prac_blockFeed_keyResp_allKeys[_prac_blockFeed_keyResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_blockFeedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_blockFeedRoutineEnd() {
  return async function () {
    //------Ending Routine 'prac_blockFeed'-------
    prac_blockFeedComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(prac_blockFeed_keyResp.corr, level);
    }
    psychoJS.experiment.addData('prac_blockFeed_keyResp.keys', prac_blockFeed_keyResp.keys);
    if (typeof prac_blockFeed_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_blockFeed_keyResp.rt', prac_blockFeed_keyResp.rt);
        routineTimer.reset();
        }
    
    prac_blockFeed_keyResp.stop();
    // the Routine "prac_blockFeed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var blockNumText;
var _task_blockReminders_keyResp_allKeys;
var task_blockRemindersComponents;
function task_blockRemindersRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'task_blockReminders'-------
    t = 0;
    task_blockRemindersClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    blockCounter = (blockCounter + 1);
    if ((blockCounter === 1)) {
        blockNumText = "Block 1 of 10";
    } else {
        if ((blockCounter === 2)) {
            blockNumText = "Block 2 of 10";
        } else {
            if ((blockCounter === 3)) {
                blockNumText = "Block 3 of 10";
            } else {
                if ((blockCounter === 4)) {
                    blockNumText = "Block 4 of 10";
                } else {
                    if ((blockCounter === 5)) {
                        blockNumText = "Block 5 of 10";
                    } else {
                        if ((blockCounter === 6)) {
                            blockNumText = "Block 6 of 10";
                        } else {
                            if ((blockCounter === 7)) {
                                blockNumText = "Block 7 of 10";
                            } else {
                                if ((blockCounter === 8)) {
                                    blockNumText = "Block 8 of 10";
                                } else {
                                    if ((blockCounter === 9)) {
                                        blockNumText = "Block 9 of 10";
                                    } else {
                                        if ((blockCounter === 10)) {
                                            blockNumText = "Block 10 of 10";
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    task_blockText.setText(blockNumText);
    task_blockReminders_keyResp.keys = undefined;
    task_blockReminders_keyResp.rt = undefined;
    _task_blockReminders_keyResp_allKeys = [];
    // keep track of which components have finished
    task_blockRemindersComponents = [];
    task_blockRemindersComponents.push(task_blockText);
    task_blockRemindersComponents.push(task_blockReminders_text);
    task_blockRemindersComponents.push(task_blockReminders_keyResp);
    
    task_blockRemindersComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function task_blockRemindersRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'task_blockReminders'-------
    // get current time
    t = task_blockRemindersClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *task_blockText* updates
    if (t >= 0.0 && task_blockText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_blockText.tStart = t;  // (not accounting for frame time here)
      task_blockText.frameNStart = frameN;  // exact frame index
      
      task_blockText.setAutoDraw(true);
    }

    
    // *task_blockReminders_text* updates
    if (t >= 0.0 && task_blockReminders_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_blockReminders_text.tStart = t;  // (not accounting for frame time here)
      task_blockReminders_text.frameNStart = frameN;  // exact frame index
      
      task_blockReminders_text.setAutoDraw(true);
    }

    
    // *task_blockReminders_keyResp* updates
    if (t >= 0.0 && task_blockReminders_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_blockReminders_keyResp.tStart = t;  // (not accounting for frame time here)
      task_blockReminders_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { task_blockReminders_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { task_blockReminders_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { task_blockReminders_keyResp.clearEvents(); });
    }

    if (task_blockReminders_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = task_blockReminders_keyResp.getKeys({keyList: ['right'], waitRelease: false});
      _task_blockReminders_keyResp_allKeys = _task_blockReminders_keyResp_allKeys.concat(theseKeys);
      if (_task_blockReminders_keyResp_allKeys.length > 0) {
        task_blockReminders_keyResp.keys = _task_blockReminders_keyResp_allKeys[_task_blockReminders_keyResp_allKeys.length - 1].name;  // just the last key pressed
        task_blockReminders_keyResp.rt = _task_blockReminders_keyResp_allKeys[_task_blockReminders_keyResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    task_blockRemindersComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function task_blockRemindersRoutineEnd() {
  return async function () {
    //------Ending Routine 'task_blockReminders'-------
    task_blockRemindersComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(task_blockReminders_keyResp.corr, level);
    }
    psychoJS.experiment.addData('task_blockReminders_keyResp.keys', task_blockReminders_keyResp.keys);
    if (typeof task_blockReminders_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('task_blockReminders_keyResp.rt', task_blockReminders_keyResp.rt);
        routineTimer.reset();
        }
    
    task_blockReminders_keyResp.stop();
    // the Routine "task_blockReminders" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _task1_stim_keyResp_allKeys;
var task_stimRoutineComponents;
function task_stimRoutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'task_stimRoutine'-------
    t = 0;
    task_stimRoutineClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ISIRange = linspace(1000, 1500, 500);
    shuffle(ISIRange);
    thisISI = (ISIRange[0] / 1000);
    console.log("thisISI: ", thisISI);
    trials.addData("ISI", thisISI);
    
    bigFace_2.setImage(straightFace);
    task_centerImg.setPos(locationC);
    task_centerImg.setSize(imageSize);
    task_centerImg.setImage(middleStim);
    task_rightImg1.setPos(locationR);
    task_rightImg1.setSize(imageSize);
    task_rightImg1.setImage(rightStim);
    task_rightImg2.setPos([0.077, 0]);
    task_rightImg2.setSize(imageSize);
    task_rightImg2.setImage(rightStim);
    task_leftImg1.setPos(locationL);
    task_leftImg1.setSize(imageSize);
    task_leftImg1.setImage(leftStim);
    task_leftImg2.setPos([(- 0.077), 0]);
    task_leftImg2.setSize(imageSize);
    task_leftImg2.setImage(leftStim);
    task_fixImg.setImage('img/transp_fixation.png');
    task1_stim_keyResp.keys = undefined;
    task1_stim_keyResp.rt = undefined;
    _task1_stim_keyResp_allKeys = [];
    // keep track of which components have finished
    task_stimRoutineComponents = [];
    task_stimRoutineComponents.push(bigFace_2);
    task_stimRoutineComponents.push(cover_background);
    task_stimRoutineComponents.push(task_centerImg);
    task_stimRoutineComponents.push(task_rightImg1);
    task_stimRoutineComponents.push(task_rightImg2);
    task_stimRoutineComponents.push(task_leftImg1);
    task_stimRoutineComponents.push(task_leftImg2);
    task_stimRoutineComponents.push(task_fixImg);
    task_stimRoutineComponents.push(task1_stim_keyResp);
    
    task_stimRoutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function task_stimRoutineRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'task_stimRoutine'-------
    // get current time
    t = task_stimRoutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *bigFace_2* updates
    if (t >= 0.0 && bigFace_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bigFace_2.tStart = t;  // (not accounting for frame time here)
      bigFace_2.frameNStart = frameN;  // exact frame index
      
      bigFace_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + thisISI - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (bigFace_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      bigFace_2.setAutoDraw(false);
    }
    
    // *cover_background* updates
    if (t >= 0.0 && cover_background.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cover_background.tStart = t;  // (not accounting for frame time here)
      cover_background.frameNStart = frameN;  // exact frame index
      
      cover_background.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.35 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cover_background.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cover_background.setAutoDraw(false);
    }
    
    // *task_centerImg* updates
    if (t >= 0.15 && task_centerImg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_centerImg.tStart = t;  // (not accounting for frame time here)
      task_centerImg.frameNStart = frameN;  // exact frame index
      
      task_centerImg.setAutoDraw(true);
    }

    frameRemains = 0.15 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (task_centerImg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      task_centerImg.setAutoDraw(false);
    }
    
    // *task_rightImg1* updates
    if (t >= 0.0 && task_rightImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_rightImg1.tStart = t;  // (not accounting for frame time here)
      task_rightImg1.frameNStart = frameN;  // exact frame index
      
      task_rightImg1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.35 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (task_rightImg1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      task_rightImg1.setAutoDraw(false);
    }
    
    // *task_rightImg2* updates
    if (t >= 0.0 && task_rightImg2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_rightImg2.tStart = t;  // (not accounting for frame time here)
      task_rightImg2.frameNStart = frameN;  // exact frame index
      
      task_rightImg2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.35 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (task_rightImg2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      task_rightImg2.setAutoDraw(false);
    }
    
    // *task_leftImg1* updates
    if (t >= 0.0 && task_leftImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_leftImg1.tStart = t;  // (not accounting for frame time here)
      task_leftImg1.frameNStart = frameN;  // exact frame index
      
      task_leftImg1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.35 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (task_leftImg1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      task_leftImg1.setAutoDraw(false);
    }
    
    // *task_leftImg2* updates
    if (t >= 0.0 && task_leftImg2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_leftImg2.tStart = t;  // (not accounting for frame time here)
      task_leftImg2.frameNStart = frameN;  // exact frame index
      
      task_leftImg2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.35 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (task_leftImg2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      task_leftImg2.setAutoDraw(false);
    }
    
    // *task_fixImg* updates
    if (t >= 0.0 && task_fixImg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_fixImg.tStart = t;  // (not accounting for frame time here)
      task_fixImg.frameNStart = frameN;  // exact frame index
      
      task_fixImg.setAutoDraw(true);
    }

    frameRemains = 0.0 + thisISI - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (task_fixImg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      task_fixImg.setAutoDraw(false);
    }
    
    // *task1_stim_keyResp* updates
    if (t >= 0.0 && task1_stim_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task1_stim_keyResp.tStart = t;  // (not accounting for frame time here)
      task1_stim_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { task1_stim_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { task1_stim_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { task1_stim_keyResp.clearEvents(); });
    }

    frameRemains = 0.0 + thisISI - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (task1_stim_keyResp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      task1_stim_keyResp.status = PsychoJS.Status.FINISHED;
  }

    if (task1_stim_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = task1_stim_keyResp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _task1_stim_keyResp_allKeys = _task1_stim_keyResp_allKeys.concat(theseKeys);
      if (_task1_stim_keyResp_allKeys.length > 0) {
        task1_stim_keyResp.keys = _task1_stim_keyResp_allKeys.map((key) => key.name);  // storing all keys
        task1_stim_keyResp.rt = _task1_stim_keyResp_allKeys.map((key) => key.rt);
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    task_stimRoutineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function task_stimRoutineRoutineEnd() {
  return async function () {
    //------Ending Routine 'task_stimRoutine'-------
    task_stimRoutineComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(task1_stim_keyResp.corr, level);
    }
    psychoJS.experiment.addData('task1_stim_keyResp.keys', task1_stim_keyResp.keys);
    if (typeof task1_stim_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('task1_stim_keyResp.rt', task1_stim_keyResp.rt);
        }
    
    task1_stim_keyResp.stop();
    trialNum = (trialNum + 1);
    if (task1_stim_keyResp.keys) {
        if ((task1_stim_keyResp.keys[0] === "left")) {
            if ((target === "left")) {
                accuracy = 1;
                numCorr = (numCorr + 1);
            } else {
                if ((target === "right")) {
                    accuracy = 0;
                }
            }
        } else {
            if ((task1_stim_keyResp.keys[0] === "right")) {
                if ((target === "right")) {
                    accuracy = 1;
                    numCorr = (numCorr + 1);
                } else {
                    if ((target === "left")) {
                        accuracy = 0;
                    }
                }
            }
        }
    }
    task_trial_loop.addData("accuracy", accuracy);
    
    // the Routine "task_stimRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var blockFeed;
var blockFeedCat;
var _task_blockFeed_keyResp_allKeys;
var task_blockFeedComponents;
function task_blockFeedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'task_blockFeed'-------
    t = 0;
    task_blockFeedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    blockAcc = (numCorr / trialNum);
    if ((blockCounter < 10)) {
        if ((blockAcc >= 0.75)) {
            if ((blockAcc < 0.9)) {
                blockFeed = "Good job";
                blockFeedCat = 1;
            } else {
                if ((blockAcc >= 0.9)) {
                    blockFeed = "Respond faster";
                    blockFeedCat = 2;
                }
            }
        } else {
            if ((blockAcc < 0.75)) {
                blockFeed = "Respond more accurately";
                blockFeedCat = 3;
            }
        }
    } else {
        if ((blockCounter === 10)) {
            /* You have completed all blocks */
        }
    }
    task_trial_loop.addData("blockFeedCat", blockFeedCat);
    trialNum = 0;
    numCorr = 0;
    
    task_blockFeed_text.setText(blockFeed);
    task_blockFeed_text2.setText('Press the right button');
    task_blockFeed_keyResp.keys = undefined;
    task_blockFeed_keyResp.rt = undefined;
    _task_blockFeed_keyResp_allKeys = [];
    // keep track of which components have finished
    task_blockFeedComponents = [];
    task_blockFeedComponents.push(task_blockFeed_text);
    task_blockFeedComponents.push(task_blockFeed_text2);
    task_blockFeedComponents.push(task_blockFeed_keyResp);
    
    task_blockFeedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function task_blockFeedRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'task_blockFeed'-------
    // get current time
    t = task_blockFeedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *task_blockFeed_text* updates
    if (t >= 0.0 && task_blockFeed_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_blockFeed_text.tStart = t;  // (not accounting for frame time here)
      task_blockFeed_text.frameNStart = frameN;  // exact frame index
      
      task_blockFeed_text.setAutoDraw(true);
    }

    
    // *task_blockFeed_text2* updates
    if (t >= 10 && task_blockFeed_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_blockFeed_text2.tStart = t;  // (not accounting for frame time here)
      task_blockFeed_text2.frameNStart = frameN;  // exact frame index
      
      task_blockFeed_text2.setAutoDraw(true);
    }

    
    // *task_blockFeed_keyResp* updates
    if (t >= 10 && task_blockFeed_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      task_blockFeed_keyResp.tStart = t;  // (not accounting for frame time here)
      task_blockFeed_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { task_blockFeed_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { task_blockFeed_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { task_blockFeed_keyResp.clearEvents(); });
    }

    if (task_blockFeed_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = task_blockFeed_keyResp.getKeys({keyList: ['right'], waitRelease: false});
      _task_blockFeed_keyResp_allKeys = _task_blockFeed_keyResp_allKeys.concat(theseKeys);
      if (_task_blockFeed_keyResp_allKeys.length > 0) {
        task_blockFeed_keyResp.keys = _task_blockFeed_keyResp_allKeys[_task_blockFeed_keyResp_allKeys.length - 1].name;  // just the last key pressed
        task_blockFeed_keyResp.rt = _task_blockFeed_keyResp_allKeys[_task_blockFeed_keyResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    task_blockFeedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function task_blockFeedRoutineEnd() {
  return async function () {
    //------Ending Routine 'task_blockFeed'-------
    task_blockFeedComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(task_blockFeed_keyResp.corr, level);
    }
    psychoJS.experiment.addData('task_blockFeed_keyResp.keys', task_blockFeed_keyResp.keys);
    if (typeof task_blockFeed_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('task_blockFeed_keyResp.rt', task_blockFeed_keyResp.rt);
        routineTimer.reset();
        }
    
    task_blockFeed_keyResp.stop();
    // the Routine "task_blockFeed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fixation1Components;
function fixation1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'fixation1'-------
    t = 0;
    fixation1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    psychoJS.eventManager.clearEvents();
    
    // keep track of which components have finished
    fixation1Components = [];
    fixation1Components.push(fix);
    
    fixation1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function fixation1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fixation1'-------
    // get current time
    t = fixation1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix* updates
    if (t >= 0.0 && fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix.tStart = t;  // (not accounting for frame time here)
      fix.frameNStart = frameN;  // exact frame index
      
      fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixation1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixation1RoutineEnd() {
  return async function () {
    //------Ending Routine 'fixation1'-------
    fixation1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _errorN_key_resp_2_allKeys;
var errorNumbers_2Components;
function errorNumbers_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'errorNumbers_2'-------
    t = 0;
    errorNumbers_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.eventManager.clearEvents();
    
    textbox_2.setText('');
    textbox_2.refresh();
    errorN_key_resp_2.keys = undefined;
    errorN_key_resp_2.rt = undefined;
    _errorN_key_resp_2_allKeys = [];
    // keep track of which components have finished
    errorNumbers_2Components = [];
    errorNumbers_2Components.push(errorNumbers_text_2);
    errorNumbers_2Components.push(textbox_2);
    errorNumbers_2Components.push(errorN_key_resp_2);
    
    errorNumbers_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function errorNumbers_2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'errorNumbers_2'-------
    // get current time
    t = errorNumbers_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *errorNumbers_text_2* updates
    if (t >= 0.0 && errorNumbers_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      errorNumbers_text_2.tStart = t;  // (not accounting for frame time here)
      errorNumbers_text_2.frameNStart = frameN;  // exact frame index
      
      errorNumbers_text_2.setAutoDraw(true);
    }

    
    // *textbox_2* updates
    if (t >= 0.0 && textbox_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_2.tStart = t;  // (not accounting for frame time here)
      textbox_2.frameNStart = frameN;  // exact frame index
      
      textbox_2.setAutoDraw(true);
    }

    
    // *errorN_key_resp_2* updates
    if (t >= 0.0 && errorN_key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      errorN_key_resp_2.tStart = t;  // (not accounting for frame time here)
      errorN_key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { errorN_key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { errorN_key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { errorN_key_resp_2.clearEvents(); });
    }

    if (errorN_key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = errorN_key_resp_2.getKeys({keyList: ['c'], waitRelease: false});
      _errorN_key_resp_2_allKeys = _errorN_key_resp_2_allKeys.concat(theseKeys);
      if (_errorN_key_resp_2_allKeys.length > 0) {
        errorN_key_resp_2.keys = _errorN_key_resp_2_allKeys[_errorN_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        errorN_key_resp_2.rt = _errorN_key_resp_2_allKeys[_errorN_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    errorNumbers_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function errorNumbers_2RoutineEnd() {
  return async function () {
    //------Ending Routine 'errorNumbers_2'-------
    errorNumbers_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('textbox_2.text',textbox_2.text)
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(errorN_key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('errorN_key_resp_2.keys', errorN_key_resp_2.keys);
    if (typeof errorN_key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('errorN_key_resp_2.rt', errorN_key_resp_2.rt);
        routineTimer.reset();
        }
    
    errorN_key_resp_2.stop();
    // the Routine "errorNumbers_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _botherRate_key_resp_allKeys;
var botherRateComponents;
function botherRateRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'botherRate'-------
    t = 0;
    botherRateClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.eventManager.clearEvents();
    
    textbox_3.setText('');
    textbox_3.refresh();
    botherRate_key_resp.keys = undefined;
    botherRate_key_resp.rt = undefined;
    _botherRate_key_resp_allKeys = [];
    // keep track of which components have finished
    botherRateComponents = [];
    botherRateComponents.push(botherRate_text);
    botherRateComponents.push(textbox_3);
    botherRateComponents.push(botherRate_key_resp);
    
    botherRateComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function botherRateRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'botherRate'-------
    // get current time
    t = botherRateClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *botherRate_text* updates
    if (t >= 0.0 && botherRate_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      botherRate_text.tStart = t;  // (not accounting for frame time here)
      botherRate_text.frameNStart = frameN;  // exact frame index
      
      botherRate_text.setAutoDraw(true);
    }

    
    // *textbox_3* updates
    if (t >= 0.0 && textbox_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_3.tStart = t;  // (not accounting for frame time here)
      textbox_3.frameNStart = frameN;  // exact frame index
      
      textbox_3.setAutoDraw(true);
    }

    
    // *botherRate_key_resp* updates
    if (t >= 0.0 && botherRate_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      botherRate_key_resp.tStart = t;  // (not accounting for frame time here)
      botherRate_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { botherRate_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { botherRate_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { botherRate_key_resp.clearEvents(); });
    }

    if (botherRate_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = botherRate_key_resp.getKeys({keyList: ['c'], waitRelease: false});
      _botherRate_key_resp_allKeys = _botherRate_key_resp_allKeys.concat(theseKeys);
      if (_botherRate_key_resp_allKeys.length > 0) {
        botherRate_key_resp.keys = _botherRate_key_resp_allKeys[_botherRate_key_resp_allKeys.length - 1].name;  // just the last key pressed
        botherRate_key_resp.rt = _botherRate_key_resp_allKeys[_botherRate_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    botherRateComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function botherRateRoutineEnd() {
  return async function () {
    //------Ending Routine 'botherRate'-------
    botherRateComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('textbox_3.text',textbox_3.text)
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(botherRate_key_resp.corr, level);
    }
    psychoJS.experiment.addData('botherRate_key_resp.keys', botherRate_key_resp.keys);
    if (typeof botherRate_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('botherRate_key_resp.rt', botherRate_key_resp.rt);
        routineTimer.reset();
        }
    
    botherRate_key_resp.stop();
    // the Routine "botherRate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var askExperimenterComponents;
function askExperimenterRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'askExperimenter'-------
    t = 0;
    askExperimenterClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    askExperimenterComponents = [];
    
    askExperimenterComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function askExperimenterRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'askExperimenter'-------
    // get current time
    t = askExperimenterClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    askExperimenterComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function askExperimenterRoutineEnd() {
  return async function () {
    //------Ending Routine 'askExperimenter'-------
    askExperimenterComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "askExperimenter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _instruct_surp1_key_resp_allKeys;
var surpriseInstructComponents;
function surpriseInstructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'surpriseInstruct'-------
    t = 0;
    surpriseInstructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instruct_surp1_key_resp.keys = undefined;
    instruct_surp1_key_resp.rt = undefined;
    _instruct_surp1_key_resp_allKeys = [];
    // keep track of which components have finished
    surpriseInstructComponents = [];
    surpriseInstructComponents.push(instruct_surprise1);
    surpriseInstructComponents.push(instruct_surp1_key_resp);
    
    surpriseInstructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function surpriseInstructRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'surpriseInstruct'-------
    // get current time
    t = surpriseInstructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruct_surprise1* updates
    if (t >= 0.0 && instruct_surprise1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruct_surprise1.tStart = t;  // (not accounting for frame time here)
      instruct_surprise1.frameNStart = frameN;  // exact frame index
      
      instruct_surprise1.setAutoDraw(true);
    }

    
    // *instruct_surp1_key_resp* updates
    if (t >= 0.0 && instruct_surp1_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruct_surp1_key_resp.tStart = t;  // (not accounting for frame time here)
      instruct_surp1_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instruct_surp1_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instruct_surp1_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instruct_surp1_key_resp.clearEvents(); });
    }

    if (instruct_surp1_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instruct_surp1_key_resp.getKeys({keyList: ['right'], waitRelease: false});
      _instruct_surp1_key_resp_allKeys = _instruct_surp1_key_resp_allKeys.concat(theseKeys);
      if (_instruct_surp1_key_resp_allKeys.length > 0) {
        instruct_surp1_key_resp.keys = _instruct_surp1_key_resp_allKeys[_instruct_surp1_key_resp_allKeys.length - 1].name;  // just the last key pressed
        instruct_surp1_key_resp.rt = _instruct_surp1_key_resp_allKeys[_instruct_surp1_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    surpriseInstructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function surpriseInstructRoutineEnd() {
  return async function () {
    //------Ending Routine 'surpriseInstruct'-------
    surpriseInstructComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(instruct_surp1_key_resp.corr, level);
    }
    psychoJS.experiment.addData('instruct_surp1_key_resp.keys', instruct_surp1_key_resp.keys);
    if (typeof instruct_surp1_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instruct_surp1_key_resp.rt', instruct_surp1_key_resp.rt);
        routineTimer.reset();
        }
    
    instruct_surp1_key_resp.stop();
    // the Routine "surpriseInstruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _instructMainTask_keyResp_allKeys;
var instructSurpriseTask2_2Components;
function instructSurpriseTask2_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instructSurpriseTask2_2'-------
    t = 0;
    instructSurpriseTask2_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instructMainTask_text.setText(taskTextSource);
    instructMainTask_keyResp.keys = undefined;
    instructMainTask_keyResp.rt = undefined;
    _instructMainTask_keyResp_allKeys = [];
    // keep track of which components have finished
    instructSurpriseTask2_2Components = [];
    instructSurpriseTask2_2Components.push(instructMainTask_text);
    instructSurpriseTask2_2Components.push(instructMainTask_keyResp);
    
    instructSurpriseTask2_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructSurpriseTask2_2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instructSurpriseTask2_2'-------
    // get current time
    t = instructSurpriseTask2_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructMainTask_text* updates
    if (t >= 0.0 && instructMainTask_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructMainTask_text.tStart = t;  // (not accounting for frame time here)
      instructMainTask_text.frameNStart = frameN;  // exact frame index
      
      instructMainTask_text.setAutoDraw(true);
    }

    
    // *instructMainTask_keyResp* updates
    if (t >= 0.0 && instructMainTask_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructMainTask_keyResp.tStart = t;  // (not accounting for frame time here)
      instructMainTask_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructMainTask_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructMainTask_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructMainTask_keyResp.clearEvents(); });
    }

    if (instructMainTask_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructMainTask_keyResp.getKeys({keyList: ['right'], waitRelease: false});
      _instructMainTask_keyResp_allKeys = _instructMainTask_keyResp_allKeys.concat(theseKeys);
      if (_instructMainTask_keyResp_allKeys.length > 0) {
        instructMainTask_keyResp.keys = _instructMainTask_keyResp_allKeys[_instructMainTask_keyResp_allKeys.length - 1].name;  // just the last key pressed
        instructMainTask_keyResp.rt = _instructMainTask_keyResp_allKeys[_instructMainTask_keyResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructSurpriseTask2_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructSurpriseTask2_2RoutineEnd() {
  return async function () {
    //------Ending Routine 'instructSurpriseTask2_2'-------
    instructSurpriseTask2_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(instructMainTask_keyResp.corr, level);
    }
    psychoJS.experiment.addData('instructMainTask_keyResp.keys', instructMainTask_keyResp.keys);
    if (typeof instructMainTask_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instructMainTask_keyResp.rt', instructMainTask_keyResp.rt);
        routineTimer.reset();
        }
    
    instructMainTask_keyResp.stop();
    // the Routine "instructSurpriseTask2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _surprise_key_resp_allKeys;
var surpriseTaskComponents;
function surpriseTaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'surpriseTask'-------
    t = 0;
    surpriseTaskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    stimulus.setImage(surpriseFaces);
    instructsurpA1_right.setPos([0.6, (- 0.03)]);
    instructsurpA1_right.setText(instructsurpA1);
    instructsurpA2_left.setText(instructsurpA2);
    surprise_key_resp.keys = undefined;
    surprise_key_resp.rt = undefined;
    _surprise_key_resp_allKeys = [];
    // keep track of which components have finished
    surpriseTaskComponents = [];
    surpriseTaskComponents.push(stimulus);
    surpriseTaskComponents.push(instructsurpA1_right);
    surpriseTaskComponents.push(instructsurpA2_left);
    surpriseTaskComponents.push(surprise_key_resp);
    
    surpriseTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function surpriseTaskRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'surpriseTask'-------
    // get current time
    t = surpriseTaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stimulus* updates
    if (t >= 0.0 && stimulus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimulus.tStart = t;  // (not accounting for frame time here)
      stimulus.frameNStart = frameN;  // exact frame index
      
      stimulus.setAutoDraw(true);
    }

    
    // *instructsurpA1_right* updates
    if (t >= 0.0 && instructsurpA1_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructsurpA1_right.tStart = t;  // (not accounting for frame time here)
      instructsurpA1_right.frameNStart = frameN;  // exact frame index
      
      instructsurpA1_right.setAutoDraw(true);
    }

    
    // *instructsurpA2_left* updates
    if (t >= 0.0 && instructsurpA2_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructsurpA2_left.tStart = t;  // (not accounting for frame time here)
      instructsurpA2_left.frameNStart = frameN;  // exact frame index
      
      instructsurpA2_left.setAutoDraw(true);
    }

    
    // *surprise_key_resp* updates
    if (t >= 0.0 && surprise_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      surprise_key_resp.tStart = t;  // (not accounting for frame time here)
      surprise_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { surprise_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { surprise_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { surprise_key_resp.clearEvents(); });
    }

    if (surprise_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = surprise_key_resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _surprise_key_resp_allKeys = _surprise_key_resp_allKeys.concat(theseKeys);
      if (_surprise_key_resp_allKeys.length > 0) {
        surprise_key_resp.keys = _surprise_key_resp_allKeys[_surprise_key_resp_allKeys.length - 1].name;  // just the last key pressed
        surprise_key_resp.rt = _surprise_key_resp_allKeys[_surprise_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    surpriseTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function surpriseTaskRoutineEnd() {
  return async function () {
    //------Ending Routine 'surpriseTask'-------
    surpriseTaskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(surprise_key_resp.corr, level);
    }
    psychoJS.experiment.addData('surprise_key_resp.keys', surprise_key_resp.keys);
    if (typeof surprise_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('surprise_key_resp.rt', surprise_key_resp.rt);
        routineTimer.reset();
        }
    
    surprise_key_resp.stop();
    // the Routine "surpriseTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _instruct_surp1_key_resp_2_allKeys;
var friendlyInstruct1Components;
function friendlyInstruct1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'friendlyInstruct1'-------
    t = 0;
    friendlyInstruct1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instruct_surp1_key_resp_2.keys = undefined;
    instruct_surp1_key_resp_2.rt = undefined;
    _instruct_surp1_key_resp_2_allKeys = [];
    // keep track of which components have finished
    friendlyInstruct1Components = [];
    friendlyInstruct1Components.push(instruct_surprise1_2);
    friendlyInstruct1Components.push(instruct_surp1_key_resp_2);
    
    friendlyInstruct1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function friendlyInstruct1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'friendlyInstruct1'-------
    // get current time
    t = friendlyInstruct1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruct_surprise1_2* updates
    if (t >= 0.0 && instruct_surprise1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruct_surprise1_2.tStart = t;  // (not accounting for frame time here)
      instruct_surprise1_2.frameNStart = frameN;  // exact frame index
      
      instruct_surprise1_2.setAutoDraw(true);
    }

    
    // *instruct_surp1_key_resp_2* updates
    if (t >= 0.0 && instruct_surp1_key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruct_surp1_key_resp_2.tStart = t;  // (not accounting for frame time here)
      instruct_surp1_key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instruct_surp1_key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instruct_surp1_key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instruct_surp1_key_resp_2.clearEvents(); });
    }

    if (instruct_surp1_key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = instruct_surp1_key_resp_2.getKeys({keyList: ['right'], waitRelease: false});
      _instruct_surp1_key_resp_2_allKeys = _instruct_surp1_key_resp_2_allKeys.concat(theseKeys);
      if (_instruct_surp1_key_resp_2_allKeys.length > 0) {
        instruct_surp1_key_resp_2.keys = _instruct_surp1_key_resp_2_allKeys[_instruct_surp1_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        instruct_surp1_key_resp_2.rt = _instruct_surp1_key_resp_2_allKeys[_instruct_surp1_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    friendlyInstruct1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function friendlyInstruct1RoutineEnd() {
  return async function () {
    //------Ending Routine 'friendlyInstruct1'-------
    friendlyInstruct1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(instruct_surp1_key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('instruct_surp1_key_resp_2.keys', instruct_surp1_key_resp_2.keys);
    if (typeof instruct_surp1_key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instruct_surp1_key_resp_2.rt', instruct_surp1_key_resp_2.rt);
        routineTimer.reset();
        }
    
    instruct_surp1_key_resp_2.stop();
    // the Routine "friendlyInstruct1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _instructMainTask_keyResp_2_allKeys;
var friendlyInstruct2Components;
function friendlyInstruct2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'friendlyInstruct2'-------
    t = 0;
    friendlyInstruct2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instructMainTask_text_2.setText(taskTextSource);
    instructMainTask_keyResp_2.keys = undefined;
    instructMainTask_keyResp_2.rt = undefined;
    _instructMainTask_keyResp_2_allKeys = [];
    // keep track of which components have finished
    friendlyInstruct2Components = [];
    friendlyInstruct2Components.push(instructMainTask_text_2);
    friendlyInstruct2Components.push(instructMainTask_keyResp_2);
    
    friendlyInstruct2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function friendlyInstruct2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'friendlyInstruct2'-------
    // get current time
    t = friendlyInstruct2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructMainTask_text_2* updates
    if (t >= 0.0 && instructMainTask_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructMainTask_text_2.tStart = t;  // (not accounting for frame time here)
      instructMainTask_text_2.frameNStart = frameN;  // exact frame index
      
      instructMainTask_text_2.setAutoDraw(true);
    }

    
    // *instructMainTask_keyResp_2* updates
    if (t >= 0.0 && instructMainTask_keyResp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructMainTask_keyResp_2.tStart = t;  // (not accounting for frame time here)
      instructMainTask_keyResp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructMainTask_keyResp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructMainTask_keyResp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructMainTask_keyResp_2.clearEvents(); });
    }

    if (instructMainTask_keyResp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructMainTask_keyResp_2.getKeys({keyList: ['right'], waitRelease: false});
      _instructMainTask_keyResp_2_allKeys = _instructMainTask_keyResp_2_allKeys.concat(theseKeys);
      if (_instructMainTask_keyResp_2_allKeys.length > 0) {
        instructMainTask_keyResp_2.keys = _instructMainTask_keyResp_2_allKeys[_instructMainTask_keyResp_2_allKeys.length - 1].name;  // just the last key pressed
        instructMainTask_keyResp_2.rt = _instructMainTask_keyResp_2_allKeys[_instructMainTask_keyResp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    friendlyInstruct2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function friendlyInstruct2RoutineEnd() {
  return async function () {
    //------Ending Routine 'friendlyInstruct2'-------
    friendlyInstruct2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(instructMainTask_keyResp_2.corr, level);
    }
    psychoJS.experiment.addData('instructMainTask_keyResp_2.keys', instructMainTask_keyResp_2.keys);
    if (typeof instructMainTask_keyResp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instructMainTask_keyResp_2.rt', instructMainTask_keyResp_2.rt);
        routineTimer.reset();
        }
    
    instructMainTask_keyResp_2.stop();
    // the Routine "friendlyInstruct2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _friendly_key_resp_allKeys;
var friendlyTaskComponents;
function friendlyTaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'friendlyTask'-------
    t = 0;
    friendlyTaskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    stimulus12.setImage(surpriseFaces);
    instructsurpA1_right_2.setPos([0.6, (- 0.03)]);
    instructsurpA1_right_2.setText(instructsurpA1);
    instructsurpA2_left_2.setText(instructsurpA2);
    friendly_key_resp.keys = undefined;
    friendly_key_resp.rt = undefined;
    _friendly_key_resp_allKeys = [];
    // keep track of which components have finished
    friendlyTaskComponents = [];
    friendlyTaskComponents.push(stimulus12);
    friendlyTaskComponents.push(instructsurpA1_right_2);
    friendlyTaskComponents.push(instructsurpA2_left_2);
    friendlyTaskComponents.push(friendly_key_resp);
    
    friendlyTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function friendlyTaskRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'friendlyTask'-------
    // get current time
    t = friendlyTaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stimulus12* updates
    if (t >= 0.0 && stimulus12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimulus12.tStart = t;  // (not accounting for frame time here)
      stimulus12.frameNStart = frameN;  // exact frame index
      
      stimulus12.setAutoDraw(true);
    }

    
    // *instructsurpA1_right_2* updates
    if (t >= 0.0 && instructsurpA1_right_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructsurpA1_right_2.tStart = t;  // (not accounting for frame time here)
      instructsurpA1_right_2.frameNStart = frameN;  // exact frame index
      
      instructsurpA1_right_2.setAutoDraw(true);
    }

    
    // *instructsurpA2_left_2* updates
    if (t >= 0.0 && instructsurpA2_left_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructsurpA2_left_2.tStart = t;  // (not accounting for frame time here)
      instructsurpA2_left_2.frameNStart = frameN;  // exact frame index
      
      instructsurpA2_left_2.setAutoDraw(true);
    }

    
    // *friendly_key_resp* updates
    if (t >= 0.0 && friendly_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      friendly_key_resp.tStart = t;  // (not accounting for frame time here)
      friendly_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { friendly_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { friendly_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { friendly_key_resp.clearEvents(); });
    }

    if (friendly_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = friendly_key_resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _friendly_key_resp_allKeys = _friendly_key_resp_allKeys.concat(theseKeys);
      if (_friendly_key_resp_allKeys.length > 0) {
        friendly_key_resp.keys = _friendly_key_resp_allKeys[_friendly_key_resp_allKeys.length - 1].name;  // just the last key pressed
        friendly_key_resp.rt = _friendly_key_resp_allKeys[_friendly_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    friendlyTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function friendlyTaskRoutineEnd() {
  return async function () {
    //------Ending Routine 'friendlyTask'-------
    friendlyTaskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (psychoJS.experiment.currentLoop instanceof MultiStairHandler) {
      psychoJS.experiment.currentLoop.addResponse(friendly_key_resp.corr, level);
    }
    psychoJS.experiment.addData('friendly_key_resp.keys', friendly_key_resp.keys);
    if (typeof friendly_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('friendly_key_resp.rt', friendly_key_resp.rt);
        routineTimer.reset();
        }
    
    friendly_key_resp.stop();
    // the Routine "friendlyTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var finishMessageComponents;
function finishMessageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'finishMessage'-------
    t = 0;
    finishMessageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    finishMessageComponents = [];
    finishMessageComponents.push(finishMessage_text);
    
    finishMessageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function finishMessageRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'finishMessage'-------
    // get current time
    t = finishMessageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *finishMessage_text* updates
    if (t >= 0.0 && finishMessage_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      finishMessage_text.tStart = t;  // (not accounting for frame time here)
      finishMessage_text.frameNStart = frameN;  // exact frame index
      
      finishMessage_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (finishMessage_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      finishMessage_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    finishMessageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function finishMessageRoutineEnd() {
  return async function () {
    //------Ending Routine 'finishMessage'-------
    finishMessageComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
